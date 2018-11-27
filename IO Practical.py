# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:18:19 2018

@author: Siu Pouvalu, 201205928
"""


import csv
import matplotlib.pyplot
import agentframework1
import random
import operator
import matplotlib.animation 

#After creating the environment, it is essential to fill it with a list 
#containing values that will be calculated using the calculations that follow


#######################################################################
####### Create environment #########
#######################################################################
environment = []
f= open("in.txt", newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    rowlist = []  
    for value in row:				# A list of value
        #print(value) 				# Floats
        rowlist.append(value)
    environment.append(rowlist) 
#f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
      
        #plot and environment        
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

#######################################################################


#######################################################################
####### Make agents #########
#######################################################################
#making the agents and connecting them to the environment
agents = []
num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20

for i in range(num_of_agents):
    agents.append(agentframework1.Agent(environment, agents)) 
                    #this line commands a connection between 
                    #the agents with the environment
       
#######################################################################


#######################################################################
####### Agent communication ###########
#######################################################################
#The following commands the agents to move and eat at the same time
                    #in their location. Agents will also search or
                    #know the location of nearby agents to share
                    
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
#######################################################################        
        


#######################################################################
####### Plotting the agents #########
#######################################################################
#The agents are plotted in the environment
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(299, 0)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
#######################################################################    


#######################################################################
############# Animating the model######################################
######################################################################

#The following code creates an animation of the model, agents moving around
#according to number of iterations. Then the code specifies a stop condition
#where agent animation stops once condition is fulfilled

num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
    
    carry_on = True	

def update(frame_number):
    
    fig.clear()
    global carry_on

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
                
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")  #once condition is met, animation stops
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1



#The next command animates the model in a loop based on number of iterations
        #but has been commented out for this session
        
        
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,
                             #repeat=False, frames=num_of_iterations)



#The next command animates the model but will stop when condition is met    
                             
animation = matplotlib.animation.FuncAnimation(fig, update, 
                                               frames=gen_function, 
                                               repeat=False)

matplotlib.pyplot.show() 


#####################################################################





"""
Created on Tue Nov 20 13:14:11 2018

@author: gy18sifp
"""

  
