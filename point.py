import math

class Point3D:
    Npts = 0
    Mx = 0
    My = 0
    Mz = 0
    
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        Point3D.Npts += 1

        
        if x > Point3D.Mx:
            Point3D.Mx = x
        if y > Point3D.My:
            Point3D.My = y
        if z > Point3D.Mz:
            Point3D.Mz = z

    @staticmethod
    def verifier_points(x, y, z):
        return (x == y == z)   
    
    @classmethod
    def getNpts(cls):
        return cls.Npts
    
    @classmethod
    def getMaxX(cls):
        return cls.Mx
    
    @classmethod
    def getMaxY(cls):
        return cls.My
    
    @classmethod
    def getMaxZ(cls):
        return cls.Mz
    
    def __str__(self):
        return f'les coordonnées sont x: {self.__x}, y: {self.__y}, z: {self.__z}'
    


# p1 = Point3D(2, 3, 4)
# print(p1.__x)  
p1 = Point3D(2, 3, 4)
p2 = Point3D(10, -1, 0)
p3 = Point3D(7, 8, 9)

print("Nombre de points :", Point3D.getNpts())  
print("Max X :", Point3D.getMaxX())              
print("Max Y :", Point3D.getMaxY())              
print("Max Z :", Point3D.getMaxZ())             

print(Point3D.verifier_points(5, 5, 5))   
print(Point3D.verifier_points(1, 2, 3))  



    
    

   

