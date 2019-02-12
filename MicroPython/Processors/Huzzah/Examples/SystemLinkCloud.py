import machine, network, ubinascii, ujson, urequests

WiFi = network.WLAN(network.STA_IF)


mac = ubinascii.hexlify(network.WLAN().config("mac"),":").decode()
print("MAC address: " + mac)
def connect():
     import network, utime
     
     WiFi = network.WLAN(network.STA_IF)
     if not WiFi.isconnected():
          print ("Connecting ..")
          WiFi.active(True)
          WiFi.connect("Tufts_Wireless","")
          i=0
          while i < 25 and not WiFi.isconnected():
               utime.sleep_ms(200)
               i=i+1
          if WiFi.isconnected():
               print ("Connection succeeded")
          else:
               print ("Connection failed")
     else:
          print ("Network Settings:", WiFi.ifconfig())
     
     
     

connect()
print ("WiFi: ",WiFi.isconnected())
# Info
Tag = "test"
Type = "STRING"
Value = "0.000000"

urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
urlTag = urlBase + Tag
urlValue = urlBase + Tag + "/values/current"

headers = {"Content-Type":"application/json","Accept":"application/json","x-ni-api-key":"ITT_X7qSzpwV0mLFf66y8swVPATu4SHYmP4g5kpYBl"}
propName={"type":Type,"path":Tag}
propValue = {"value":{"type":Type,"value":Value}}

# PUT
print(urequests.put(urlTag,headers=headers,json=propName).text)
print(urequests.put(urlValue,headers=headers,json=propValue).text)
# Info
Tag = "test"
Type = "STRING"
Value = "0.000000"

urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
urlTag = urlBase + Tag
urlValue = urlBase + Tag + "/values/current"

headers = {"Content-Type":"application/json","Accept":"application/json","x-ni-api-key":"ITT_X7qSzpwV0mLFf66y8swVPATu4SHYmP4g5kpYBl"}
propName={"type":Type,"path":Tag}
propValue = {"value":{"type":Type,"value":Value}}

## GET
value = urequests.get(urlValue,headers=headers).text

data = ujson.loads(value)
result = data.get("value").get("value")
print ("value = ",result)
