#!/usr/bin/python3

import math


def angle(point):
    '''
    returns angle[rad, 0-2PI] between horizontal axis and point's polar coordinate
    input: 2D point coordinates represented by list [horizontal_coordinate, vertical coordinate]
    '''
    # limit 90deg
    if point[0]==0 and point[1]>0:
        return math.pi/2
    # limit 270deg
    elif point[0]==0 and point[1]<0:
        return math.pi*3/2
    # the first quadrant
    elif point[0]>0 and point[1]>=0:
        return math.atan(point[1]/point[0])
    # the second & third quadrant
    elif point[0]<0:
        return math.pi + math.atan(point[1]/point[0])
    # the fourth quadrant
    elif point[0]>0 and point[1]<0:
        return 2*math.pi + math.atan(point[1]/point[0])
    else:
        return 0


def lenght(point):
    '''
    returns lenght of polar
    input: 2D point coordinates represented by list [horizontal_coordinate, vertical coordinate]    
    '''
    return math.sqrt(pow(point[0],2)+pow(point[1],2))


def coord(lenght, angle):
    '''
    returns point [x,y] from polar lenght and angle
    '''
    return [lenght*math.cos(angle), lenght*math.sin(angle)]


def trans2D(point, d_angle):
    '''
    give new point coordinates after rotation about delta angle
    '''
    curr_point_angle = angle(point)
    curr_point_lenght = lenght(point)

    new_point_angle = curr_point_angle + d_angle
    new_point = coord(curr_point_lenght, new_point_angle)

    return new_point


def test_trans():
    while 1:
        x = float(input('set horizontal coordinate: '))
        y = float(input('set vertical coordinate: '))
        alfa = float(input('set delta rotation: [deg]'))*math.pi/180
        point = [x,y]
        print('The angle of point {0} is {1}rad,  =  {2}deg'.format(point, round(angle(point),4), round(angle(point)/(math.pi/180),3)))
        print('polar lenght:', lenght(point))
        print('coord:',coord( lenght(point), angle(point)))
        print()
        print('new point coordinates after rotation about {0}deg / {1}rad are: {2}'.format(alfa/(math.pi/180), alfa, trans2D(point, alfa)))


def plus_angle(angle):
    if angle < 0:
        return 360 + angle
    else:
        return angle

point3D = [0.0,0.0,1.0]

trans_angles = [-90,-45,-0]
trans_angles[0] = plus_angle(trans_angles[0])
trans_angles[1] = plus_angle(trans_angles[1])
trans_angles[2] = plus_angle(trans_angles[2])
print('plused angles:', trans_angles)


# back rotation about Z

angle_rot = -1 * trans_angles[2] # reverse rot angle
rotated_2Dpoint = trans2D([point3D[0],point3D[1]],angle_rot)
point3D[0] = rotated_2Dpoint[0]
point3D[1] = rotated_2Dpoint[1]
print('point after reverse rotation about Z:', point3D)


# back rotation about X

angle_rot = -1 * trans_angles[0] # reverse rot angle
rotated_2Dpoint = trans2D([point3D[1],point3D[2]],angle_rot)
point3D[1] = rotated_2Dpoint[0]
point3D[2] = rotated_2Dpoint[1]
print('point after reverse rotation about X:', point3D)


# back rotation about Y

angle_rot = -1 * trans_angles[1] # reverse rot angle
rotated_2Dpoint = trans2D([point3D[2],point3D[0]],angle_rot)
point3D[2] = rotated_2Dpoint[0]
point3D[0] = rotated_2Dpoint[1]
print('point after reverse rotation about Y:', point3D)


















