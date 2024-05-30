import paho.mqtt.client as mqtt
import time
from pydexarm import Dexarm
import time


'''host = "127.0.0.1"
port = 1883
client = mqtt.Client()
client.connect(host)'''

'''windows'''
dexarm = Dexarm(port="COM7")
'''mac & linux'''
# device = Dexarm(port="/dev/tty.usbmodem3086337A34381")


def co_(x,y,z):
    dexarm.move_to(x, y, z)
    txt = '{"x": '+str(x)+', "y": '+str(y)+', "z": '+str(z)+'}'

    '''client.publish("test/test",txt)'''
    while 1 :
        position = dexarm.get_current_position()
        print(position)
        if(position[0] == x and position[1]==y and position[2]==z):
            return position

        
dexarm.go_home()

co_(50,300,-50)

dexarm.air_picker_pick()

co_(50,300,-50)

co_(50,300,0)

co_(-50,300,0)

co_(-50,300,-50)

dexarm.air_picker_nature()

dexarm.go_home()



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