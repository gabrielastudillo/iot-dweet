import time
import requests

# This example sends fixed artificial temperature values 
# to http://dweet.io/, a IoT on Cloud API Service.
# with name = gastudillo_raspi
#
# To check this dweet, visit here on browser
# http://dweet.io/follow/gastudillo_raspi
#
dweetIO = "https://dweet.io/dweet/for/" #common url for all users (post) 
myThing = "gastudillo_raspi" #replace with you OWN thing name
   
n = 15 #starting counter
temp = 50  #init temp
humidity = 10 #init humidity

while n > 0:
    rqsString = dweetIO+myThing+'?'+'temperature='+str(temp)+'&'+'humidity='+str(humidity)
    print(rqsString) #url for post
    rqs = requests.post(rqsString) #posting
    print (rqs.status_code) #printing response status
    print (rqs.headers) #print response headers
    print (rqs.content) #print response content
    time.sleep(5) #5 seconds pause
    temp += 1.5 
    humidity += 10
    n -= 1
