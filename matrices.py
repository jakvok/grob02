#!/usr/bin/python3

import numpy as np
import math 

alf = 315.0 * math.pi / 180 # rot angle axis X
bet = 270.0 * math.pi / 180 # rot angle axis Y
gam = 0.0 * math.pi / 180 # rot angle axis Z

p = [0.0, 0.0, 1.0] # input point

# 2D tranform matrix axis Z
Txy = np.array([[round(math.cos(gam),6), round(-1*math.sin(gam),6), 0],
                [round(math.sin(gam),6), round(math.cos(gam),6), 0],
                [0, 0, 1]])
print('Z axis trans matrix:\n {}\n'.format(Txy))

# 2D tranform matrix axis Y
Txz = np.array([[round(math.cos(bet),6), 0, round(math.sin(bet),6)],
                [0, 1, 0],
                [round(-1*math.sin(bet),6), 0, round(math.cos(bet),6)]])
print('Y axis trans matrix:\n {}\n'.format(Txz))

# 2D tranform matrix axis X
Tyz = np.array([[1, 0, 0],
                [0, round(math.cos(alf),6), round(-1*math.sin(alf),6)],
                [0, round(math.sin(alf),6), round(math.cos(alf),6)]])
print('X axis trans matrix:\n {}\n'.format(Tyz))

# total tranform matrix axes Y -> X -> Z
T = Txz @ Tyz @ Txy
print('Full 3D trans matrix T, Y -> X -> Z\n{}\n'.format(T))


q = np.dot(T, p) # output point

print(p,' = point before transformation\n',
      q,' = point after transformation')