import sys
sys.path.insert(0, '../..')

import pyrosim
import math

sim = pyrosim.Simulator(play_paused=True,debug=True,eval_time=5000)


#for i in range(10):
#    segment = sim.send_cylinder(x=0,y=(-0.5-i),z=0.5, r=0,g=1,b=0,length=0.5,r1=0,r2=1,r3=0,radius=0.1,)

segment = [sim.send_cylinder(x=0,y=(0.5+i),z=0.5, r=((i+1)%2),g=(i%2),b=(i*3%2),length=.9,r1=0,r2=1,r3=0,radius=0.1) for i in range (10)]

joint = [sim.send_hinge_joint(first_body_id=segment[i],second_body_id=segment[i+1],x=0,y=i+1,z=.5,n1=((i+1)%2),n2=0,n3=(i%2)) for i in range(9)]

sensor = [sim.send_touch_sensor(body_id=segment[i]) for i in range(10)]

sneuron = [sim.send_sensor_neuron(sensor[i]) for i in range(10)]

mneuron = [sim.send_motor_neuron(joint[i]) for i in range(9)]

synapse = [sim.send_developing_synapse(sneuron[i],mneuron[i],start_weight=-10,end_weight=10,start_time=0, end_time=1) for i in range(9)]

sim.start()
