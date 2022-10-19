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
        int valor= math.sqrt(((self.get_X)**2+(self.get_Y)**2+(self.get_Z))**2);
        return valor


    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
        return math.sqrt((point_2.get_X() - self.get_X())**2 + (point_2.get_Y - self.get_Y())**2 + (point2.get_Z - self.get_Z)**2)

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):
        if (self.get_X() == 0 or self.get_Y == 0):
            return 0;
        if (self.get_X() > 0 and self.get_Y > 0):
            return 1;
        if (self.get_X() < 0 and self.get_Y > 0):
            return 2;
        if (self.get_X() < 0 and self.get_Y < 0):
            return 3;
        if (self.get_X() > 0 and self.get_Y < 0):
            return 4;


    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        pass