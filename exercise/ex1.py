#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:37:38 2022

@author: dliu
"""

# p1
l = ['a', 2, 7, 3.0, 4.5]
print(l[-1])

# p2
l = [1, 2, 3, 4, 5, 6, 7]
l2 = l[1:]
print(l2)

# p3
l = [67, 87, 34, 67, 99]
l2 = l[1:-1]
print(l2)

# p4
l = [67, 87, 34, 67, 99]
l[-1] += 100
print(l)

# p5
l = [67, 87, 34, 67, 99]
l.insert(0, 52)
print(l)

# p6
l = [67, 87, 34, 67, 99]
l.insert(2, -27)
print(l)

# p7
l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]
del l[l.index('Per')]
print(l)

# p8
l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]
l.remove('Sven')
print(l)

# p9
l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]
l = l[2:]
print(l)

# p10
l = []
for i in range(5):
    l.append([42]*6)
print(l[2][2])
    
# p11
phone_book = {'Arne': 47329823,
              'Bengt': 91238129,
              'Stina': 1928319,
              'Lena': 98129312}

# p12
print(list(range(2,5,8)))   ##??

# p13
l = [45, 78, 90, 34, 23]
for i in l:
    print(i)

# p14
for i in range(13):
    print(i)

# p15
l = [45, 78, 90, 34, 23]
for i in l[::2]:
    print(i)

# p16
a = [3, 6, 8, 10, 34, 32]
b = [76, 45, 10, 6, 89, 11]
c = []
for i,j in zip(a,b):
    c.append(i+j)
print(c)

# p17
nested_list = [[1, 2, 3], [4, 5, 6, 7, 8, 9], [10, 11]]
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        print(nested_list[i][j])

# p18
from math import sqrt, ceil

for n in range(2,101):
    end = ceil(sqrt(n))
    if end==2:
        if n%2==0:
            print(f'{n} is not prime')
        else:
            print(f'{n} is prime')
    else:
        flag = True
        for i in range(2,end+1):
            if n%i==0:
                print(f'{n} is not prime')
                flag = False
                break
        if flag:
            print(f'{n} is prime')

# p19
def prime_detector(n):
    end = ceil(sqrt(n))
    if end==2:
        if n%2==0:
            return False
        else:
            return True
    else:
        for i in range(2,end+1):
            if n%i==0:
                return False
        return True

for n in range(2,101):
    if prime_detector(n):
        print(f'{n} is prime')
    else:
        print(f'{n} is not prime')

# p20
def negative(l):
    return [i for i in l if i<0]

from random import randint
l = [randint(-100,101) for i in range(100)]
print(negative(l))

# p21
from math import sin
def f(x):
    return sin(x)
def derivative(fn,x,h):
    return (fn(x)-fn(x+h))/h

derivative(f, 1, .1)


# p22
from math import sin

def f(x):
    return sin(x)

def f_table(f, start, end, length):
    print('x f(x)')
    x = start
    while x<=end:
        print('{:.4f} {:.4f}'.format(x, f(x)))
        x += length
    
f_table(f, -6.2832, -5.9832, .1)


# p23
l = [
    [45, 78, 56, 34],
    [9, 23, 23],
    [34, 87],
    [12, 19, 78, 56, 45]
]

f = open('file.txt', 'w')
for i in range(len(l)):
    for j in range(len(l[i])):
        f.write(str(l[i][j])+' ')
    f.write('\n')
f.close()


# p24
l = []

f = open('file.txt', 'r')
lines = f.readlines()
for line in lines:
    l.append([int(i) for i in line.strip().split(' ')])

print(l)











