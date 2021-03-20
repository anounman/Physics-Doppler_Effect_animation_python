'''
Deppler Effect Animation 
Devloped By Ankush Das
Date : - 19 March 2021
Language : - Visual Python
'''
from sys import argv
from vpython import *
sobject = box(pos=vector(-6,0,0),color=color.red)

movement = (int(argv[1]))
sound = 2.0
ring_count = 0
incress_by = 0.1
ring_incres_by = 0.1
scene.background = color.white

frequency_wave = [ring(pos=sobject.pos, axis=vector(0,0,1),
         radius=0.5, thickness=0.1,color=color.blue)]
while True:
    rate(10)
    if (ring_count >= 1.0):
      frequency_wave.append(ring(pos=sobject.pos, axis=vector(0,0,1),
      radius=0.5, thickness=0.1,color=color.blue))
      ring_count = 0
    sobject.pos.x += movement*incress_by
    for waves in frequency_wave:
      waves.radius += sound*incress_by
      if waves.radius >= 15:
        waves.visible = False
        del  waves
    ring_count += ring_incres_by
