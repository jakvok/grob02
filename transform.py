#!/usr/bin/python3

import numpy as np
import math 

class Transform3D:
    
    def __init__(self, angles = [0.0,0.0,0.0], sequence='yxz'):
        sequence = sequence.lower()
        if len(sequence) == 3:
            self.sequence = sequence
        self.angles = []
        for n in angles:
            self.angles.append(n * math.pi / 180)
        self.matrix = self.__matrix()

    def __matrix(self):
        # 2D tranform matrix axis Z
        Txy = np.array([[round(math.cos(self.angles[2]),6), round(-1*math.sin(self.angles[2]),6), 0],
                        [round(math.sin(self.angles[2]),6), round(math.cos(self.angles[2]),6), 0],
                        [0, 0, 1]])
        
        # 2D tranform matrix axis Y
        Txz = np.array([[round(math.cos(self.angles[1]),6), 0, round(math.sin(self.angles[1]),6)],
                        [0, 1, 0],
                        [round(-1*math.sin(self.angles[1]),6), 0, round(math.cos(self.angles[1]),6)]])
        
        # 2D tranform matrix axis X
        Tyz = np.array([[1, 0, 0],
                        [0, round(math.cos(self.angles[0]),6), round(-1*math.sin(self.angles[0]),6)],
                        [0, round(math.sin(self.angles[0]),6), round(math.cos(self.angles[0]),6)]])

        matrixes = []
        for char in self.sequence:
            if char == 'x': matrixes.append(Tyz)
            elif char == 'y': matrixes.append(Txz)
            elif char == 'z': matrixes.append(Txy)
            else: raise Exception('current sequence not allowed')

        # total tranform matrix axes
        return matrixes[0] @ matrixes[1] @ matrixes[2]

    def transform(self, point=[0.0,0.0,0.0]):
        return np.dot(self.matrix, point)

a = Transform3D([-31.367,-37.562,55.908],'yXz')
#print(a.sequence)
#print(a.angles)
#print(a.matrix)
print(a.transform([0,0,0.05]))
