import sys
sys.path.insert(0, '../..')

import pyrosim

sim = pyrosim.Simulator(debug=True,eval_time=1000)

leg1 = sim.send_cylinder(x=0,y=0,z=1, r=0,g=1,b=0, r1=0,r2=1,r3=0, length=1.5, radius=0.1)
leg2 = sim.send_cylinder(x=0,y=-0.5,z=1, r=0,g=1,b=1, r1=0,r2=0,r3=1,length=1, radius=0.1)

sensor1 = sim.send_touch_sensor(body_id=leg1)
sensor2 = sim.send_touch_sensor(body_id=leg2)

joint1=sim.send_hinge_joint(first_body_id = leg1, second_body_id = leg2,
                            x=0,y=-0.5,z=1, n1=-1,n2=0,n3=0, lo=-2/4,hi=2/4)

sneuron1 = sim.send_sensor_neuron(sensor1)
sneuron2 = sim.send_sensor_neuron(sensor2)

mneuron = sim.send_motor_neuron(joint1)

sim.send_synapse(sneuron1,mneuron, weight=20)
sim.send_synapse(sneuron2,mneuron, weight=-5)

sim.start()
sim.wait_to_finish()
print sim.get_sensor_data(sensor1, svi=0)
print sim.get_sensor_data(sensor2, svi=0)
