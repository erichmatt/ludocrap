import sys
sys.path.insert(0, '../..')

import pyrosim
import math

sim = pyrosim.Simulator(play_paused=True,debug=True,eval_time=5000)

segment = sim.send_cylinder(x=0,y=-0.5,z=0.5, r=0,g=1,b=0,length=0.5,
                         r1=0,r2=1,r3=0,radius=0.1,)

for i in range(10):
    segment = sim.send_cylinder(x=0,y=(-0.5-i),z=0.5, r=0,g=1,b=0,length=0.5,
                         r1=0,r2=1,r3=0,radius=0.1,)

print("boobies",segment)
sim.start()
