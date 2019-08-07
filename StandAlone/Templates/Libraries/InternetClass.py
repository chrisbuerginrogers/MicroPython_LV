import machine, network, ubinascii, ujson, urequests, utime
import passwords

class wifi():
     def __init__(self):
          self.WiFi = network.WLAN()
          self.mac = ubinascii.hexlify(network.WLAN().config("mac"),":").decode()
          print("MAC address: " + self.mac)
          self.TW_urlBase = "https://ptcacademic-dev3-twx.es.thingworx.com/Thingworx/"
          self.TW_headers = {"Accept":"application/json","Content-Type":"application/json","AppKey":passwords.Keys['Thingworx']}
          self.SL_urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
          self.SL_headers = {"Accept":"application/json","x-ni-api-key":passwords.Keys['SystemLink']}
          while not self.wifiConnect(2):
               utime.sleep(1)
               print ('Trying Again...')
          return

     def wifiConnect(self,timeout = 2):
          EN1 = machine.Pin("W23", machine.Pin.OUT, value=1)  # set power high for USB power (500mA now allowed)
          print ("Connecting to SSID %s" % (passwords.wifi['username']))
          self.WiFi.active(True)
          self.WiFi.connect(passwords.wifi['username'],passwords.wifi['password'])
          starttime = utime.time()
          while ((utime.time()-starttime) < timeout) and not self.WiFi.isconnected():
               utime.sleep_ms(200)
          return self.WiFi.isconnected()

     def close(self):
          return self.WiFi.disconnect()
     
     def TW_Put(self,thing, property, type, value):
          urlValue = self.TW_urlBase + 'Things/' + thing + '/Properties/*'
          propValue = {property:value}
          #  assume that the tag is already created  -      urequests.put(urlTag,headers=headers,json=propName).text
          try:
               response = urequests.put(urlValue,headers=self.TW_headers,json=propValue)
               print(response.text)
               response.close()
               return True
          except Exception as e:
               print(e)
               return False

     def TW_Get(self,thing, property):
          urlValue = self.TW_urlBase + 'Things/' + thing + '/Properties/' + property
          try:
               response = urequests.get(urlValue,headers=self.TW_headers)
               value = response.text
               response.close()
               data = ujson.loads(value)
               result = data.get("rows")[0].get(property)
          except Exception as e:
               print(e)
               result = e
          return result
          
     def SL_Put(self, Tag, Type, Value):
          urlTag = self.SL_urlBase + Tag
          urlValue = self.SL_urlBase + Tag + "/values/current"
          propName={"type":Type,"path":Tag}
          propValue = {"value":{"type":Type,"value":Value}}
          try:
               response = urequests.put(urlTag,headers=self.SL_headers,json=propName).text
               response = urequests.put(urlValue,headers=self.SL_headers,json=propValue).text
               response.close()
               return True
          except Exception as e:
               print(e)
               return False
               
     def SL_Get(self, Tag):
          urlValue = self.SL_urlBase + Tag + "/values/current"
          try:
               value = urequests.get(urlValue,headers=self.SL_headers).text
               data = ujson.loads(value)
               result = data.get("value").get("value")
               print ("value = ",result)
               return True , result
          except Exception as e:
               print (e)
               return False ,''
