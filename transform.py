#!/usr/bin/python3

import numpy as np
import math 

class Transform3D:
    '''
    Object represents rotation tranformation between two coordinate systems.
    arguments:  angles = list of three values, angle rotations by axis X, Y, Z in degrees. Plus direction is CCW.
                sequence = string of three chars, sequence of axes rotations, default <yxz>.
    methods: transform(point), point = list of three point's coordinates x, y, z in base coord system. Method returns list of three values, transformed coordinates of point after rotation.   
    '''

    
    def __init__(self, angles = [0.0,0.0,0.0], sequence='yxz'):
        sequence = sequence.lower()
        if len(sequence) == 3 and 'x' in sequence and 'y' in sequence and 'z' in sequence:
            self.sequence = sequence # sequence of axes rotations
        else: raise Exception('Not allowed sequence string.')
        self.angles = [] # transformation's rotation angles by axes X, Y, Z
        if type(angles) is list and len(angles) == 3:
            for n in angles:
                try:
                    self.angles.append(n * math.pi / 180) # angles in radians
                except ValueError:
                    print('Angle values are not a number.')
                    raise ValueError
        else: raise Exception('Three values of rotation expected.')
        self.matrix = self.__matrix() # transformation matrix


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
        for char in self.sequence: # correct sequence of 2D rotation matrixes
            if char == 'x': matrixes.append(Tyz)
            elif char == 'y': matrixes.append(Txz)
            elif char == 'z': matrixes.append(Txy)
            else: raise Exception('current sequence not allowed')

        # total 3D transform matrix axes
        return matrixes[0] @ matrixes[1] @ matrixes[2]


    def transform(self, point=[0.0,0.0,0.0]):
        '''
        input: list of 3 point coordinates in base coord system
        output: list of 3 point coordinates in rotated coord system
        '''
        return np.dot(self.matrix, point)


a = Transform3D([-31.367,-37.562,55.908],'yXz')
#print(a.sequence)
#print(a.angles)
#print(a.matrix)
print(a.transform([0,0,0.05]))
