
#from abc import ABCMeta, abstractmethod
import abc
from math import pi, sqrt
import numpy as np

class Shape(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, *coords):
        super(Shape, self).__init__()
        self._coords = list(map(list, *coords))
        
    @abc.abstractmethod
    def area(self):
        """Abstract, will never be initiated/returned"""
        return

    @abc.abstractmethod
    def perimeter(self):
        """Abstract, will never be initiated/returned"""
        return
    
    def __getitem__(self, key):
        return self._coords[key]

    def __len__(self):
        return len(self._coords)
    
    def move(self,distance):
        for i in range(len(self)):
            self._coords[i][0] += distance[0]
            self._coords[i][1] += distance[1]


########################        
class Circle(Shape):
    def __init__(self, coords, radius):
        self._coords = list(coords)
        self.radius = radius
    
    def area(self):
        return pi * self.radius**2
        
    def perimeter(self):
        return 2 * pi * self.radius
        
    def intersects(self, other):
        return (self.radius-other.radius)**2 <=\
        (self._coords[0]-other._coords[0])**2 + \
        (self._coords[1]-other._coords[1])**2 <= (self.radius+other.radius)**2
        

########################        
class Line(Shape):
    def __init__(self, *coords):
        super(Line, self).__init__(coords)

    def area(self):
        return 0
        
    def perimeter(self):
        return 0
    
    def __len__(self):
        return len(self._coords)
    
    def length(self):
        length = 0 
        for i in range(len(self) - 1):
            length += sqrt((self[i][0]-self[i+1][0])**2 + 
                        (self[i][1]-self[i+1][1])**2)
        return float(length)

    @staticmethod
    def _direction(p_i, p_j, p_k):
        tmp1 = [p_k[0] - p_i[0], p_k[1] - p_i[1]]
        tmp2 = [p_j[0] - p_i[0], p_j[1] - p_i[1]]
        return tmp1[0] * tmp2[1] - tmp1[1] * tmp2[0]

    
    @staticmethod
    def _intersects(p1, p2, p3, p4):
        d1 = Line._direction(p3, p4, p2)
        d2 = Line._direction(p3, p4, p1)
        d3 = Line._direction(p1, p2, p3)
        d4 = Line._direction(p1, p2, p4)
        
        if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
            return True
        elif d1 == 0 and _on_segment(p3, p4, p1):
            return True
        elif d2 == 0 and _on_segment(p3, p4, p2):
            return True
        elif d3 == 0 and _on_segment(p1, p2, p3):
            return True
        elif d4 == 0 and _on_segment(p1, p2, p4):
            return True
        else:
            return False

    
    @staticmethod
    def _on_segment(p_i, p_j, p_k):
        if min(p_i[0], p_j[0]) <= p_k[0] <= max(p_i[0], p_j[0]) and min(p_i[1], p_j[1]) <= p_k[1] <= max(p_i[1], p_j[1]):
            return True
        else:
            return False

        
    def intersects(self, line):
        p1 = self._coords[0]
        p2 = self._coords[1]
        p3 = line._coords[0]
        p4 = line._coords[1]

        return Line._intersects(p1, p2, p3, p4)


##########################    
class Point(Shape):
    def __init__(self, *coords):
        super(Point, self).__init__(coords)
    
    def area(self):
        return 0
        
    def perimeter(self):
        return 0

###########################
#Assuming no holes (as said) and ordered input data
class Polygon(Shape):
    def __init__(self, *coords):
        super(Polygon, self).__init__(coords)
    
    
    def area(self): #shoelace formula
        x,y = zip(*p._coords)[0], zip(*p._coords)[1]
        return np.abs(np.dot(x[:len(x)-1],y[1:])-np.dot(y[:len(y)-1],x[1:]))/2
        
        
    def perimeter(self):
        per = 0
        for i in range(len(self)-1):
            per += sqrt((self[i][0]-self[i+1][0])**2 + 
                        (self[i][1]-self[i+1][1])**2) 
        return per

#######################
class PolyLine(Line):
    def __init__(self, *coords):
        super(PolyLine, self).__init__(*coords)
        
    def intersects(self, p):
        self_line_segs = [Line(self[i],self[i+1]) for i in range(len(self)-1)]
        p_line_segs = [Line(p[i],p[i+1]) for i in range(len(p)-1)]
        for i in range(len(self_line_segs)):
            for j in range(len(p_line_segs)):
                if self_line_segs[i].intersects(p_line_segs[j]):
                    return True
        return False

#######################    
class Square(Polygon):
    def __init__(self, coords, side):
        super(Square, self).__init__(coords)
        self.side = side
    
    def area(self):
        return self.side ** 2
        
    def perimeter(self):
        return self.side * 4

#######################    
class Triangle(Polygon):
    def __init__(self, *coords):
        super(Triangle, self).__init__(*coords)
        #NEED TO ADD EXTRA TO ALSO START/END WITH SAME COORDINATES:
        self._coords = self._coords + [self._coords[0]] 

    def area(self):
        s = self.perimeter()/2
        len_arr = []
        for i in range(len(self) - 1):
            len_arr.append(sqrt((self[i][0]-self[i+1][0])**2 + 
                        (self[i][1]-self[i+1][1])**2))
        a = sqrt(s*(s-len_arr[0])*(s-len_arr[1])*(s-len_arr[2]))
        return a


############################################################################
############################################################################
############################################################################
############################################################################
if __name__ == '__main__':
    # Tests for circle
    # ===================================
    c1 = Circle((0, 0), 1)
    
    assert c1.area() == pi
    assert c1.perimeter() == 2 * pi
    
    c2 = Circle((3, 0), 1)
    
    assert not c1.intersects(c2)
    assert not c2.intersects(c1)
    
    c2.radius = 2.5 # Increase the radius
    
    assert c1.intersects(c2)
    assert c2.intersects(c1)
    
    print 'Success! Circle tests passed!'
    
    # Tests for line
    # ===================================
    lin1 = Line((0, 0), (0, 2))
    
    assert lin1.length() == 2.0
    
    lin2 = Line((-1, 1), (1, 1))
    assert lin2[0][0], lin2[0][1] == (-1, 1)

    assert lin1.intersects(lin2)
    assert lin2.intersects(lin1)
    
    assert lin1.area() == 0
    assert lin1.perimeter() == 0
    print 'Success! Line tests passed!'
    
    # Tests for point
    # ===================================
    p = Point((0, 0))
    assert p.area() == 0
    
    p.move((1, 1))
    assert p[0][0], p[0][1] == (1, 1) 

    assert p.perimeter() == 0
    print 'Success! Point tests passed!'
    
    # Tests for polygon - a capital "H"
    # ===================================
    p = Polygon((0, 0), (0, 5), (1, 5), (1, 3), (2, 3), (2, 5), (3, 5), (3, 0), (2, 0), (2, 2), (1, 2), (1, 0), (0, 0))
    
    assert p.area() == 11.0
    
    p.move((2, 2))
    assert p.area() == 11.0
    
    assert p.perimeter() == 24.0
    
    assert p[-1][0], p[-1][1] == (2, 2) 
    
    print 'Success! Polygon tests passed!'
    
    # Tests for polyline
    # ===================================
    p1 = PolyLine((0, 0), (2, 0))
    p2 = PolyLine((0, 1), (2, 1))
    p3 = PolyLine((-1, -1), (1, -1), (1, 2))
    
    assert not p1.intersects(p2)
    assert p1.intersects(p3)
    assert p3.intersects(p2)
        
    assert p1.length() == 2
    assert p2.length() == 2
    assert p3.length() == 5
        
    assert p1.area() == 0
        
    assert p2.perimeter() == 0
        
    assert p3[1][0], p3[1][1] == (1, -1)
    
    print 'Success! Polyline tests passed!'
    
    # Tests for square
    # ===================================
    s = Square((0, 0), 5)
    assert s.area() == 25
    
    s.move((1, 1))
    assert s[0][0], s[0][1] == (1, 1)
    
    s.side = 4

    assert s.perimeter() == 16
    print 'Success! Square tests passed!'
    
    # Tests for triangle
    # ===================================
    t = Triangle((-1, -1), (-1, -3), (-3, -1))
    
    assert t.area() - 2.0 < 6e-16 # Fix due to round-off errors
    
    assert t.perimeter() == 4.0 + sqrt(8.0)
    
    assert t[2][0], t[2][1] == (-3, -1)
    
    print 'Success! Triangle tests passed!'