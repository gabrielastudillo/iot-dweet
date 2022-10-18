import time
import dweepy


# This example sends fixed artificial temperature values 
# to http://dweet.io/, a IoT on Cloud API Service.
# with name = gastudillo_raspi
#
# To check this dweet, visit here on browser
# http://dweet.io/follow/gastudillo_raspi
#
myThing = "gastudillo_raspi" #replace with you OWN thing name
key1= "temperature"
key2= "humidity"   
n = 15 #starting counter
temp = 50  #init temp
humidity = 10 #init humidity

while n > 0:
    dweepy.dweet_for(myThing, {key1: str(temp), key2: str(humidity)})
    temp += 1.5 
    humidity += 10
    n -= 1
    time.sleep(5) #5 seconds pause
