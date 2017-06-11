# -*- coding: utf-8 -*-

import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
    def move(self, n, m):
        self.x = self.x + n
        self.y = self.y + m

class LineString(Point):
    def __init__(self, *args):
        self.points = [Point(*p) for p in args]

    def __getitem__(self, key):
        return self.points[key] 

    def move(self, n, m):
        for p in self.points:
            p.move(n,m)

    def length(self):
        length = 0 
        for i in range(len(self.points) - 1):
            length += math.sqrt((self.points[i].x-self.points[i+1].x)**2 + 
                        (self.points[i].y-self.points[i+1].y)**2)
        return float(length)

if __name__ == '__main__':
    # Tests for LineString
    # ===================================
    # Tests for LineString
    # ===================================
    lin1 = LineString((1, 1), (0, 2))
   
    assert lin1.length() == math.sqrt(2.0)
        
    lin1.move(-1, -1) # Move by -1 and -1 for x and y respectively
    
    assert lin1[0].y == 0
    #assert lin1.y[0] == 0 # Inspect the y value of the start point.
    # Implement this by overloading __getitem__(self, key) in your class.    
    
    lin2 = LineString((1, 1), (1, 2), (2, 2))

    assert lin2.length() == 2.0
    
    lin2.move(-1, -1) # Move by -1 and -1 for x and y respectively
    
    assert lin2.length() == 2.0

    assert lin2[-1].x == 1
    #assert lin2.x[-1] == 1 # Inspect the x value of the end point.
    
    print 'Success! Line tests passed!'