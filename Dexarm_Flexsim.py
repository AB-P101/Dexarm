import paho.mqtt.client as mqtt
import time
from pydexarm import Dexarm
import time


host = "127.0.0.1"
port = 1883
client = mqtt.Client()
client.connect(host)

'''windows'''
dexarm = Dexarm(port="COM7")
'''mac & linux'''
# device = Dexarm(port="/dev/tty.usbmodem3086337A34381")


def co_(x,y,z):
    time.sleep(1)
    position = dexarm.get_current_position()
    x, y, z = int(x*100), int(y*100), int(z*100)
    
    cx, cy, cz = False, False, False
    rX, rY, rZ = int(position[0]*100), int(position[1]*100), int(position[2]*100)
    while 1 :
        time.sleep(0.003)
        position = dexarm.get_current_position()
        print(position)

        if(cx == False):
            if(rX >= x-10 and rX <= x+10):
               cx = True 
            else :
                if(rX <= x):
                    rX = rX+10
                else :
                    rX = rX-10
            print('X:'+str(rX)+':'+str(x))

        if(cy == False):
            if(rY >= y-10 and rY <= y+10):
                cy = True
            else :
                if(rY <= y):
                    rY = rY+10
                else :
                    rY = rY-10
            print('Y:'+str(rY)+':'+str(y))

        if(cz == False):
            if(rZ >= z-10 and rZ <= z+10):
                cz = True
            else :
                if(rZ <= z):
                    rZ = rZ+10
                else :
                    rZ = rZ-10
            print('Z:'+str(rZ)+':'+str(rZ))

        if(cx and cy and cz) :
            return
        dexarm.move_to(rX/100, rY/100, rZ/100)
        txt = '{"x": '+str(position[4])+', "y": '+str(position[5])+', "z": '+str(position[6])+'}'
        client.publish("test/test",txt)
        
        
        
        

        


        
co_(0,300,0)

co_(200,300,-55)

#dexarm.air_picker_pick()

co_(-200,300,0)

co_(-200,300,0)

co_(-200,300,-55)
co_(-200,300,-50)

#dexarm.air_picker_nature()

co_(0,300,0)




''''client.publish("test/test",)'''

'''DexArm sliding rail Demo'''
'''
dexarm.conveyor_belt_forward(2000)
time.sleep(20)
dexarm.conveyor_belt_backward(2000)
time.sleep(10)
dexarm.conveyor_belt_stop()
'''

'''DexArm sliding rail Demo'''
'''
dexarm.go_home()
dexarm.sliding_rail_init()
dexarm.move_to(None,None,None,0)
dexarm.move_to(None,None,None,100)
dexarm.move_to(None,None,None,50)
dexarm.move_to(None,None,None,200)
'''
dexarm.close()