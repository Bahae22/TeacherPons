#from numpy import sqrt


class Point3D:

    #A point is defined by 3 coordinates


    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def __init__(self):
        self.x = x
        self.y = y
        self.z = z
    
    #x---------------    
    def get_x(self):
    	return self.x
    	
    def set_x(self, x):
    	self.x = x
    
    #y---------------
    def get_y(self):
    	return self.y
    	
    def set_y(self, y):
    	self.y = y
    
    #z---------------	
    def get_z(self):
    	return self.z
    	
    def set_z(self, z):
    	self.z = z
    
    #toString
    def __str__(self):
    	return "x: " + self.x + ", y: " + self.y + ", z:" + self.z

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
        return sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)

    #Commit 3: Distance between 2 points.
    def calculate_distance(self, point_2):
    	x2 = point_2.x
    	y2 = point_2.y
    	z2 = point_2.z
        return sqrt((x2-self.x)**2+(y2-self.y)**2+(z2-self.z)**2)

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):
        #Devuelve 0 si está en el origen de coordenadas o sobre alguno de los ejes.
        #Devuelve 1 si está en el primer cuadrante (x e y positivos).
        #Devuelve 2 si está en el segundo cuadrante (x negativo e y positivo).
        #Devuelve 3 si está en el tercer cuadrante (x e y negativos).
        #Devuelve 4 si está en el cuarto cuadrante (x positivo e y negativo).
        if self.x > 0 and self.y > 0:
        return 1
        elif self.x < 0 and self.y > 0:
        return 2
        elif self.x < 0 and self.y < 0:
        return 3
        elif self.x > 0 and self.y < 0:
        return 4
        else
        return 0 

    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        contador = 9999999
        
        for point_2 in points:
        if (math.sqrt((point_2.get_x - self.x)**2 + (point_2.get_y - self.y)**2 + (point_2.get_z - self.z)** 2) < contador):
        cont = math.sqrt((point_2.getx - self.x)** 2 + (point_2.get_y - self.y)** 2 + (point_2.get_z - self.z)**2)
        return point 2


if __name__ == "__main__":
    pass
