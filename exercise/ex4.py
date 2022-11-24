#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:22:02 2022

@author: dliu
"""

# p45
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
    
    def set(self, x, y):
        self.__x = x
        self.__y = y
    
    def move(self, dx, dy): 
        self.__x += dx
        self.__y += dy
        
    def copy_from(self, p):
        self.__x = p.x
        self.__y = p.y
        
    def __str__(self): # <---- New __str__ method
        return "Point("+str(self.__x)+", "+str(self.__y)+")"


class Rectangle(Point):
    def __init__(self, x=(0,0,0), y=(0,0,0)):
        
        self._p1 = Point(x[0],y[0])
        self._p2 = Point(x[1],y[1])
        self.flag = False
        
    @property
    def p1(self):
        return self._p1
        
    @p1.setter
    def p1(self, xy):
        self._p1.x = xy[0]
        self._p1.y = xy[1]
        
    @property
    def p2(self):
        return self._p2
        
    @p2.setter
    def p2(self, xy):
        self._p2.x = xy[0]
        self._p2.y = xy[1]
    
    @property
    def p3(self):
        if self.flag:
            return self._p3
        else:
            raise ValueError("need value for point 3")
            
        
    @p3.setter
    def p3(self, xy):
        vec1 = self.p1.x-self.p2.x, self.p1.y-self.p2.y
        vec2 = xy[0]-self.p1.x, xy[1]-self.p1.y
        vec3 = xy[0]-self.p2.x, xy[1]-self.p2.y

        if vec1[0]*vec2[0]+vec1[1]*vec2[1]!=0 and vec1[0]*vec3[0]+vec1[1]*vec3[1]!=0:        
            raise ValueError("not proper point")
            
        if vec1[0]*vec2[0]+vec1[1]*vec2[1]==0 or vec1[0]*vec3[0]+vec1[1]*vec3[1]==0:
            self._p3 = Point(xy[0], xy[1])
            self.flag = True
        
    @property
    def p4(self):
        x4 = self._p2.x+self._p3.x-self._p1.x
        y4 = self._p2.y+self._p3.y-self._p1.y
        self._p4 = Point(x4, y4)
        return self._p4
    
    
    def copy_from(self, rectangle):
        self._p1 = rectangle.p1
        self._p2 = rectangle.p2
        self._p3 = rectangle.p3

    @property
    def edge(self):
        e1 = ((self.p2.x-self.p1.x)**2+(self.p2.y-self.p1.y)**2)**.5
        e2 = ((self.p3.x-self.p2.x)**2+(self.p3.y-self.p2.y)**2)**.5
        e3 = ((self.p3.x-self.p1.x)**2+(self.p3.y-self.p1.y)**2)**.5
        
        ll = [e1, e2, e3]
        ll.sort()
        return ll
    
    @property
    def width(self):
        if self.flag:
            return self.edge[0]
        else:
            raise ValueError("not proper rectangle")
            
    @property
    def height(self):
        if self.flag:
            return self.edge[1]
        else:
            raise ValueError("not proper rectangle")

    
    def __str__(self):
        return "Rectangle("+str(self.p1)+", "+str(self.p2)+", "+str(self.p3)+", "+str(self.p4)+")"

rectangle = Rectangle()
rectangle.p1 = (0,0)
rectangle.p2 = (0,2)
rectangle.p3 = (1,0)

print(rectangle)
print(rectangle.width)
print(rectangle.height)





# Polyline
class Polyline(Point):
    def __init__(self):
        self._poly = []
    
    @property
    def poly(self):
        return self._poly
        
    def add(self, x, y):
        self._poly.append(Point(x,y))
    
    def remove(self, index):
        del self._poly[index]
    
    @property
    def clear(self):
        self._poly = []
    
    def __call__(self, idx):
        return self._poly[idx]
    
    def __str__(self):
        return "Polyline("+' '.join([str(i) for i in self._poly])+")"
    
polyline = Polyline()
polyline.add(3,2)
polyline.add(3,3)
polyline.add(3,4)
polyline.add(2,5)

polyline.remove(1)
print(polyline)

# polyline.clear
# print(polyline)




# p46
import csv 

class Geyser:
    def __init__(self, filename):
        self.filename = filename
        self.read_data()
        
    def read_data(self):
        data = []
        with open(self.filename, 'r') as file:
            flag = True
            for line in file:
                if flag:
                    head = line.rstrip().split(',')
                    flag = False
                else:
                    data.append([float(i) for i in line.rstrip().split(',')])
        
        self.data = data
    
    @property
    def data_table(self):
        return self.data
    
    def query_data(self, t):
        results = []
        for i in range(len(self.data)):
            if self.data[i][1]>t:
                results.append(self.data[i])
                
        return results
    
    # def write_data(self, head, table, filename):
    #     with open(filename, 'w') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(head)
    #         for line in table:
    #             writer.writerow(line)

# head, data = read_data('faithful.csv')

# data_4_5 = query_data(data, t=4.5)
# write_data(head, data_4_5, 'faithful_max_4_5.csv')

geyser = Geyser("faithful.csv")
print(geyser.data_table)
result_table = geyser.query_data(4.5)
print(result_table)