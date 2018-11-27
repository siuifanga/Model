import random
import operator
import matplotlib.pyplot
import time
start = time.clock()

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

  
num_of_agents = 3
num_of_iterations = 10
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
'''
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


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

distance = distance_between(agents[0], agents[1])


print(distance) 



end = time.clock()
print("time = " + str(end - start))
'''
distances = []
for m in range(num_of_agents):
    for n in range(num_of_agents):
        #this is reduce duplication, so it will only tun the calculations if m is greater than n 
        if (m>n):
            distance = distance_between(agents [m], agents [n])
            #the distances append populations the distances [] specified above
        distances.append([distance])
        print (m,n,distance)
        print(max(agents))
        print(min(agents))
#this gives us the max and min in the x direction
print(max(agents, key=operator.itemgetter(1)))
print(min(agents, key=operator.itemgetter(1)))
    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                