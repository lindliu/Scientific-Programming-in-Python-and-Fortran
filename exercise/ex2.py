#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 16:15:19 2022

@author: dliu
"""

# p37
import numpy as np
np.linspace(-np.pi, np.pi, 100)

# p38
A = np.random.randint(0, 100, [5, 5])
B = np.random.randint(0, 100, [5, 5])
C = A@B

# p39
a = np.arange(36).reshape(6,6)

print(f'1. value of row 2 column 2: {a[1,1]}')
print(f'2. row 3: {a[2,:]}')
print(f'3. column 4: {a[:,3]}')
print(f'4. the last row: {a[-1,:]}')
print(f'5. the last column: {a[:,-1]}')