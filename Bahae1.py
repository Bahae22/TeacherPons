from math import *

class Point3D:

#A point is defined by 3 coordinates
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)

    def get_X(self):
        return self.x
    
    def get_Y(self):
        return self.y
    
    def get_Z(self):
        return self.z

    def set_X(self,x):
        self.x=x
    
    def set_Y(self,y):
        self.y=y

    def set_Z(self,z):
        self.z=z

    def __str__(self):
        return "X:"+str(self.x)+" Y:"+str(self.y)+" Z:"+str(self.z)


    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return math.sqrt((pow(self.get_x()) + pow(self.get_y()) + pow(self.get_z()))


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        return math.sqrt(pow(self.get_x() - point_2.get_x(), 2) + pow(self.get_y() - point_2.get_y(), 2) + pow(self.get_z() - point_2.get_z(), 2))

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):

        if(self.x == 0 || self.y == 0 || self.z == 0):
            return 0
        elif(self.x>0):
            if(self.y>0):
                #si x e y son positivos
                return 1
            else:
                #si x es positivo e y es negativo
                return 4
        elif(self.y>0):
            #x negativo e y positivo
            return 2
        else:
            #x negativo e y negativo
            return 3


    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        pass
