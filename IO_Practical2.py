# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:39:59 2018

@author: gy18sifp
"""

import random
import operator
import matplotlib.pyplot
import agentframework1
import csv

#this function will return the distance between these two agents when it is called.
'''def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
'''

environment = []


#######################################################################
    ####### Create environment #########
#######################################################################
f= open("in.txt", newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
     rowlist = []
     environment.append(rowlist)   
     for value in row:				# A list of value
        #print(value) 				# Floats
        rowlist.append(value)
#f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

#######################################################################

 


num_of_agents = 10
num_of_iterations = 10
agents = []


# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])




# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents.append(agentframework1.Agent(environment,agents)) #connect agents with the environment
        
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

 
'''
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
'''