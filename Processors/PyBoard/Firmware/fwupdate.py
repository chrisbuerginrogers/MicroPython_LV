# Update mboot from a .dfu.gz file on the filesystem
# MIT license; Copyright (c) 2019 Damien P. George

import struct, time
import uzlib, machine

try:
    import stm
except ImportError:
    pass


FLASH_KEY1 = 0x45670123
FLASH_KEY2 = 0xcdef89ab


def check_mem_contains(addr, buf):
    mem8 = stm.mem8
    r = range(len(buf))
    for off in r:
        if mem8[addr + off] != buf[off]:
            return False
    return True

def check_mem_erased(addr, size):
    mem16 = stm.mem16
    r = range(0, size, 2)
    for off in r:
        if mem16[addr + off] != 0xffff:
            return False
    return True

def dfu_read(filename):
    f = open(filename, 'rb')

    hdr = f.read(3)
    f.seek(0)
    if hdr == b'Dfu':
        pass
    elif hdr == b'\x1f\x8b\x08':
        f = uzlib.DecompIO(f, 16 + 15)
    else:
        print('Invalid firmware', filename)
        return None

    elems = []

    hdr = f.read(11)
    sig, ver, size, num_targ = struct.unpack('<5sBIB', hdr)
    #print(sig, ver, size, num_targ)

    file_offset = 11

    for i in range(num_targ):
        hdr = f.read(274)
        sig, alt, has_name, name, t_size, num_elem = struct.unpack('<6sBi255sII', hdr)
        #print(sig, alt, has_name, name.strip(b'\x00'), t_size, num_elem)

        file_offset += 274
        file_offset_t = file_offset
        for j in range(num_elem):
            hdr = f.read(8)
            addr, e_size = struct.unpack('<II', hdr)
            #print(hex(addr), e_size)
            data = f.read(e_size)
            elems.append((addr, data))
            file_offset += 8 + e_size

        if t_size != file_offset - file_offset_t:
            print('corrupt DFU', t_size, file_offset - file_offset_t)

    if size != file_offset:
        print('corrupt DFU', size, file_offset)

    hdr = f.read(16)
    hdr = struct.unpack('<HHHH3sBI', hdr)
    #print(hdr)

    return elems

def flash_wait_not_busy():
    while stm.mem32[stm.FLASH + stm.FLASH_SR] & 1 << 16:
        machine.idle()

def flash_unlock():
    stm.mem32[stm.FLASH + stm.FLASH_KEYR] = FLASH_KEY1
    stm.mem32[stm.FLASH + stm.FLASH_KEYR] = FLASH_KEY2

def flash_lock():
    stm.mem32[stm.FLASH + stm.FLASH_CR] = 1 << 31 # LOCK

def flash_erase_sector(sector):
    assert 0 <= sector <= 7 # for F722
    flash_wait_not_busy()
    cr = (
        2 << 8 # PSIZE = 32 bits
        | sector << 3 # SNB
        | 1 << 1 # SER
    )
    stm.mem32[stm.FLASH + stm.FLASH_CR] = cr
    stm.mem32[stm.FLASH + stm.FLASH_CR] = cr | 1 << 16 # STRT
    flash_wait_not_busy()
    stm.mem32[stm.FLASH + stm.FLASH_CR] = 0

def flash_write(addr, buf):
    assert len(buf) % 4 == 0
    flash_wait_not_busy()
    cr = (
        2 << 8 # PSIZE = 32 bits
        | 1 << 0 # PG
    )
    stm.mem32[stm.FLASH + stm.FLASH_CR] = cr
    for off in range(0, len(buf), 4):
        stm.mem32[addr + off] = struct.unpack_from('I', buf, off)[0]
        flash_wait_not_busy()
    stm.mem32[stm.FLASH + stm.FLASH_CR] = 0

def update_mboot(filename):
    print('Loading file', filename)

    mboot_fw = dfu_read(filename)
    if mboot_fw is None:
        return
    if len(mboot_fw) != 1:
        assert 0
    mboot_addr, mboot_fw = mboot_fw[0]
    if mboot_addr != 0x08000000:
        assert 0

    # Validate firmware in a simple way
    # TODO

    chk = check_mem_contains(mboot_addr, mboot_fw)
    if chk:
        print('Supplied version of mboot is already on device.')
        return

    print('Programming mboot, do not turn off!')
    time.sleep_ms(50)

    irq = machine.disable_irq()
    flash_unlock()
    #print('flash unlocked')
    flash_erase_sector(0)
    #print('sector 0 erased')
    if not check_mem_erased(mboot_addr + 16 * 1024, 16 * 1024):
        flash_erase_sector(1) # not needed for F767
        #print('sector 1 erased')
    flash_write(mboot_addr, mboot_fw)
    #print('firmware written')
    flash_lock()
    machine.enable_irq(irq)

    chk = check_mem_contains(mboot_addr, mboot_fw)
    if chk:
        print('Verification of new mboot succeeded.')
    else:
        print('Verification of new mboot FAILED!  Try rerunning.')

    print('Programming finished, can now reset or turn off.')

def stage1(filename='/flash/PYBD_SF2_W4F2_mboot.dfu.gz'):
    import os, pyb
    try:
        os.stat(filename)
    except:
        print('File not found:', filename)
        return
    update_mboot(filename)
    os.remove(filename)
    print('stage1 done, rebooting')
    time.sleep(1)
    pyb.bootloader()
    # mboot will now update main firmware

def stage2(filename='/flash/PYBD_SF2_W4F2.dfu.gz'):
    # mboot has updated main firmware
    import os
    try:
        os.stat(filename)
    except:
        print('File not found:', filename)
        return
    os.remove(filename)
    print('stage2 done')
