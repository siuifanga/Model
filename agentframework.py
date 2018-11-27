'''
#shift coordinates into a list
#do some analysis on coordinates
#always place random function at the top

import random 
import matplotlib
import operator
#create containers to store agent coordinates
#shift our coordinates into lists
#do some analysis on our coordinates
y0 = random.randint(0,99)
x0 = random.randint(0,99)

#this is a more efficient way to list agents.
num_of_agents = 10

# import random
# if random_number < 0.5:
#     y0 = y0 + 1
# else:
#     y0 = y0 - 1
import random

y0 = 50
x0 = 50
# Random walk one step.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

print(y0)


y0, x0 = 50, 50
rand = random.random()
# Random walk one step.
if rand < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

print(y0)

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)


y1, x1 = 50, 50

if rand < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

print(y1)

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

'''
#Defining functions

import random
import operator
import matplotlib.pyplot

#this function will return the distance between these two agents when it is called.
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100



answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)

#calling the function defined above
distance = distance_between(agents[0], agents[1])
print(distance)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show() 

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

 
"""
Created on Tue Nov  6 14:05:47 2018

@author: gy18sifp
"""

