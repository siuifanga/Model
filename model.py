import random

y0, x0 = 50, 50
rand = random.random()

if rand < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

print(y0)
print (x0)

import random

# Set up variables.
y0 = 50
x0 = 50

# Random walk one step.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

print(y0)

import random
y0 = 50
x0 = 50
if random.random() < 0.5:
    x0 += 1
else:
    x0 -=1
print ("x0: ",x0)

import random 
y0,x0 = 50,50
rand = random.random()#
if rand < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
    print (x0)

import random
#set up variables
y0 = 50
x0 = 50
#random walk one step
if random.random () < 0.5:
    x0 += 1
else:
    x0 -= 1
print (y0)

import random
#set up variables
y0 = 50
x0 = 50
#random walk one step
if random.random () < 0.5:
    y0 += 1
else: 
    y0 -= 1
if random.random () < 0.5:
    x0 += 1
else:
    x0 -= 1
print (y0,x0)

import random

y0 = 50
x0 = 50

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)







y1 = 50
x1 = 50

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)
print ("y1 ", y1)
print ("x1 ", x1)
print ("else")
print ("if")


answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)


import random
y1 = 50
x1 = 50

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)

y0 = 0
x0 = 0
y1 = 4
x1 = 3
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)


      

