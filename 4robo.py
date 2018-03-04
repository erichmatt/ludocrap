import sys
sys.path.insert(0, '../..')

import pyrosim
import math

sim = pyrosim.Simulator(play_paused=True,debug=True,eval_time=5000)

body = sim.send_box(x=0,y=0,z=0.5,length=0.5,width=0.5,height=0.1)
leg1 = sim.send_cylinder(x=0,y=-0.5,z=0.5, r=0,g=1,b=0,length=0.5,
                         r1=0,r2=1,r3=0,radius=0.1,)
leg2 = sim.send_cylinder(x=0,y=0.5,z=0.5, r=0,g=1,b=1,length=0.5,
                         r1=0,r2=1,r3=0,radius=0.1)
leg3 = sim.send_cylinder(x=0.5,y=0,z=0.5, r=0,g=0,b=1,length=0.5,
                         r1=1,r2=0,r3=0,radius=0.1)
leg4 = sim.send_cylinder(x=-0.5,y=0,z=0.5, r=1,g=0,b=1,length=0.5,
                         r1=1,r2=0,r3=0,radius=0.1)

joint1 = sim.send_hinge_joint(first_body_id=body,second_body_id=leg1,
                              x=0,y=-0.25,z=0.5,n1=1,n2=0,n3=0)
joint2 = sim.send_hinge_joint(first_body_id=body,second_body_id=leg2,
                              x=0,y=0.25,z=0.5,n1=1,n2=0,n3=0)
joint3 = sim.send_hinge_joint(first_body_id=body,second_body_id=leg3,
                              x=0.25,y=0,z=0.5,n1=0,n2=1,n3=0)
joint4 = sim.send_hinge_joint(first_body_id=body,second_body_id=leg4,
                              x=-.250,y=0,z=0.5,n1=0,n2=1,n3=0)

sensor1=sim.send_touch_sensor(body_id=leg1)
sensor2=sim.send_touch_sensor(body_id=leg2)
sensor3=sim.send_touch_sensor(body_id=leg3)
sensor4=sim.send_touch_sensor(body_id=leg4)

sneuron1=sim.send_sensor_neuron(sensor1)
sneuron2=sim.send_sensor_neuron(sensor2)
sneuron3=sim.send_sensor_neuron(sensor3)
sneuron4=sim.send_sensor_neuron(sensor4)

mneuron1=sim.send_motor_neuron(joint1)
mneuron2=sim.send_motor_neuron(joint2)
mneuron3=sim.send_motor_neuron(joint3)
mneuron4=sim.send_motor_neuron(joint4)

fneuron1=sim.send_function_neuron(math.sin)
fneuron2=sim.send_function_neuron(math.sin)
fneuron3=sim.send_function_neuron(math.sin)
fneuron4=sim.send_function_neuron(math.sin)

#sim.send_synapse(sneuron1,mneuron1,weight=-10)
#sim.send_synapse(sneuron2,mneuron2,weight=0.5)
#sim.send_synapse(sneuron3,mneuron3,weight=-10)
#sim.send_synapse(sneuron4,mneuron4,weight=0.5)

sim.send_developing_synapse(fneuron1,mneuron1,start_weight=10,end_weight=10,
                            start_time=0, end_time=1)
sim.send_developing_synapse(fneuron2,mneuron2,start_weight=-10,end_weight=10,
                            start_time=0, end_time=1)
sim.send_developing_synapse(fneuron3,mneuron3,start_weight=10,end_weight=-10,
                            start_time=0, end_time=1)
sim.send_developing_synapse(fneuron4,mneuron4,start_weight=10,end_weight=10,
                            start_time=0, end_time=1)


sim.start()
