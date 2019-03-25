import machine, network, ubinascii, ujson, urequests, utime

WiFi = network.WLAN()


mac = ubinascii.hexlify(network.WLAN().config("mac"),":").decode()
print("MAC address: " + mac)
def connect():
     if not WiFi.isconnected():
          print ("Connecting ..")
          WiFi.active(True)
          WiFi.connect("SSID","PASSWORD")
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
Tag = "fred2"
Type = "STRING"
Value = "hi"
Key = "APIKey_HERE"

urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
     
## PUT
urlTag = urlBase + Tag
urlValue = urlBase + Tag + "/values/current"

headers = {"Accept":"application/json","x-ni-api-key":Key}
propName={"type":Type,"path":Tag}
propValue = {"value":{"type":Type,"value":Value}}

#define tag - not necessary if the tag is already defined
response = urequests.put(urlTag,headers=headers,json=propName)
print(response.text)
response.close()

#assign value
response = urequests.put(urlValue,headers=headers,json=propValue)
print(response.text)
response.close()

urlValue = urlBase + Tag + "/values/current"

## GET
response = urequests.get(urlValue,headers=headers)
value = response.text
response.close()

data = ujson.loads(value)
result = data.get("value").get("value")
print ("value = ",result)

