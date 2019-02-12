import lcd160cr, machine, utime



lcd = lcd160cr.LCD160CR("Y")# X if USB is visible and Y if covered by screen
lcd.set_orient(lcd160cr.PORTRAIT) # PORTRAIT or LANDSCAPE
lcd.set_startup_deco(lcd160cr.STARTUP_DECO_MLOGO)
lcd.set_brightness(10)
lcd.erase()
lcd.set_pos(0, 0)
lcd.set_text_color(lcd.rgb(255, 255, 255), lcd.rgb(0, 0, 0))
lcd.set_font(2)
lcd.set_pos(0, 0)

lcd.set_pos(0, 0)
lcd.write('Hello MicroPython!')
print('touch:', lcd.get_touch())

lcd.write("Code Check")
for i in range(5):
     lcd.write("i = " + str(i) + "\r\n")
     utime.sleep_ms(1000)


