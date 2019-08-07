import machine, network, ubinascii, ujson, urequests, utime

# Get wifi details and more from a passwords.py file
try:
    import passwords
except ImportError:
    print("WiFi passwords should be in your passwords.py file on the processor (Sample under Templates/Library)")
    raise

WiFi = network.WLAN()

mac = ubinascii.hexlify(network.WLAN().config("mac"),":").decode()
print("MAC address: " + mac)
def connect():
     EN1 = machine.Pin("W23", machine.Pin.OUT, value=1)  # set power high for USB power (500mA now allowed)
     if not WiFi.isconnected():
          print ("Connecting ..")
          WiFi.active(True)
          WiFi.connect(passwords.wifi['username'],passwords.wifi['password'])
          i=0
          while i < 25 and not WiFi.isconnected():
               utime.sleep_ms(200)
               i=i+1
          if WiFi.isconnected():
               print ("Connection succeeded")
          else:
               print ("Connection failed")     

connect()
print ("WiFi: ",WiFi.isconnected())

# Info
Tag = "fred"
Type = "STRING"
Value = "hello"
Key = passwords.Keys['SystemLink']

urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
     
## PUT
urlTag = urlBase + Tag
urlValue = urlBase + Tag + "/values/current"

headers = {"Accept":"application/json","x-ni-api-key":Key}
propName={"type":Type,"path":Tag}
propValue = {"value":{"type":Type,"value":Value}}

print(urequests.put(urlTag,headers=headers,json=propName).text)
print(urequests.put(urlValue,headers=headers,json=propValue).text)

urlValue = urlBase + Tag + "/values/current"

## GET
value = urequests.get(urlValue,headers=headers).text

data = ujson.loads(value)
result = data.get("value").get("value")
print ("value = ",result)

'''
######  SPIKE Code #####
import hub,utime

hub.port.B.info()

# if info comes back with None - then you have to restart the pybaord
i=0
fred = bytes([11])
while (i<15):
     try:
          i=i+1 if i<19 else 10
          value = hub.port.B.device.get()[0]
          #print(value)
          hub.display.show(str(value))
          #print(value)
          hub.port.B.device.mode(0,fred*i)
          utime.sleep(0.1)
     except:
          utime.sleep(1)
'''
