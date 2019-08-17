import RPi.GPIO as rp
import time
import sys
import Adafruit_DHT
import requests 

rp.setmode(rp.BCM)
rp.setwarnings(False)
rp.setup(4,rp.OUT)#trig pin1
rp.setup(17,rp.IN)#echo pin1
rp.setup(27,rp.OUT)#trig pin 2
rp.setup(22,rp.IN)#echo pin2
rp.setup(10,rp.IN)#ldr pin for input
rp.setup(9,rp.OUT)#bulb pin
rp.setup(5,rp.OUT)#M11
rp.setup(6,rp.OUT)#M12
rp.setup(13,rp.OUT)#M21
rp.setup(19,rp.OUT)#M22

##funtions
def caldist():
    rp.output(4,1)
    time.sleep(0.00001)
    rp.output(4,0)

    starttime = time.time()
    stoptime= time.time()
    while(rp.input(17)==0):
        starttime = time.time()
    while(rp.input(17)==1):
        stoptime = time.time()
    
    elapsedtime = stoptime-starttime

    d = 34300*elapsedtime*0.5
    return d
def caldist1():
    rp.output(27,1)
    time.sleep(0.00001)
    rp.output(27,0)

    starttime1 = time.time()
    stoptime1= time.time()
    while(rp.input(22)==0):
        starttime1 = time.time()
    while(rp.input(22)==1):
        stoptime1 = time.time()
    
    elapsedtime1 = stoptime1-starttime1

    d1= 34300*elapsedtime1*0.5
    return d1

#user input
u = int(input('enter 1 for auto and 2 for manual'))
count =0
#auto mode
if(u ==1):
    while(True):
        distance = caldist()
        if(distance<=10):
            while(distance<=10):
                distance=caldist()
            count += 1
            print('count=',count)
            time.sleep(0.1)
        if(count >0):
            if(rp.input(10) ==0):
                rp.output(9,0)#on command
            elif(rp.input(10) ==1):
                rp.output(9,1)#off command
        humidity,temperature = Adafruit_DHT.read_retry(11,11)
        print('Temp:{0:0.1f} C '.format(temperature,humidity))
        #humidity:{1:0.1f} %' .format(temperature,humidity)
        time.sleep(0.1)
        if(temperature >21):
            while(True):
                rp.output(5,1)
                rp.output(6,0)
                time.sleep(1)

    #Exit          
        distance1 = caldist1()
        if(distance1<=10):
            while(distance1<=10):
                distance1=caldist1()
            count =count-1
            print('count=',count)
            time.sleep(0.1)
            
        if(count==0):
            rp.output(9,0)
            while(True):
                rp.output(5,0)
                rp.output(6,0)

#manual mode
elif(u==2):
    while(True):
        r = requests.get('http://indianiotcloud.com/retrieve.php?id=BB5288W8LMOX9L5G1DER')
        d = r.json()
        print(d)
        d1 = int(d['result'][0]['field1'])
        d2 = int(d['result'][0]['field1'])
        d3 = int(d['result'][0]['field1'])
        d4 = int(d['result'][0]['field1'])
        if(d1==0):
            rp.output(9,1)#off command light
        elif(d1==1):
            rp.output(9,0)#on command light
        elif(d2==1):#fan on
            while(True):
                rp.output(5,1)
                rp.output(6,0)
        elif(d2==0):#fan off
            while(True):
                rp.output(5,0)
                rp.output(6,0)
        elif(d3==1):#ex fan on
            while(True):
                rp.output(13,1)
                rp.output(19,0)
        elif(d3==0):#ex fan off
            while(True):
                rp.output(13,0)
                rp.output(19,0)
        
    
        
            



    

















