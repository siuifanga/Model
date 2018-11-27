
# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
# import random



import random
import operator
import matplotlib

agents = []

y0 = random.randint(0,99)
x0 = random.randint(0,99) 
agents.append([y0,x0]) 


'''
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

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)

#code to work out the distance between the agents which are the coordinates
y0 = 0
x0 = 0
y1 = 4
x1 = 3
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)
'''

#Making containers to store agents, randomize starting locations
y0 = random.randint(0,99)
x0 = random.randint(0,99)
mostleftagent = min(agents, key=operator.itemgetter(1))
mosthighagent = max(agents, key=operator.itemgetter(0))
mostlowagent = min(agents, key=operator.itemgetter(0))
mostrightagent = max(agents, key=operator.itemgetter(1))
agents.append([random.randint(0,99),random.randint(0,99)]) 
print (y0,x0)

print(max(agents))
#this gives us the max in the x direction
print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])


matplotlib.pyplot.show()

matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='orange')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='blue')

#matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='yellow')
matplotlib.pyplot.scatter(mostlowagent[1], mostlowagent[0], color='black')
matplotlib.pyplot.scatter(mosthighagent[1], mosthighagent[0], color='grey')
matplotlib.pyplot.scatter(mostrightagent[1], mostrightagent[0], color='yellow')
matplotlib.pyplot.scatter(mostleftagent[1], mostleftagent[0], color='pink')
matplotlib.pyplot.show()


matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

#Use for-loops to reduce the code size and make the number of agents more flexible
num_of_agents = 4
num_of_iterations = 4 

#this for-loops allows us to create many loops

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
  
    print (agents)

#second loop for iteration
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents.append([random.randint(0,100),random.randint(0,100)])
  
    print (agents)
    
    if random.random() < 0.5:
        agents[0][0] += 1
    else:
        agents[0][0] -= 1

    if random.random() < 0.5:
        agents[0][1] += 1
    else:
        agents[0][1] -= 1

    if random.random() < 0.5:
       agents[0][0] += 1
    else:
        agents[0][0] -= 1

    if random.random() < 0.5:
        agents[0][1] += 1
    else:
        agents[0][1] -= 1
    print (agents)
    

# Move agent.
if random.random() < 0.5:
    agents[i][0] += 1
else:
    agents[i][0] -= 1
# Check if off edge and adjust.
if agents[i][0] < 0:
    agents[i][0] = 0
if agents[i][1] < 0:
    agents[i][0] = 0
if agents[i][0] > 99:
    agents[i][0] = 99
if agents[i][1] > 99:
    agents[i][0] = 99
    
    if random.random() < 0.5:
        agents[i][0] = (agents[i][0] + 1) % 100
    else:
        agents[i][0] = (agents[i][0] - 1) % 100
    
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()

   
# blur ---------------------------------------
import matplotlib.pyplot

data = []
processed_data = []

# Fill with random data.
for i in (range(0,99)):
    datarow = []
    for j in (range(0,99)):
        datarow.append(random.randint(0,255))
    data.append(datarow)

# Blur.
for i in (range(0,25)):
    datarow = []
    for j in (range(0,30)):
        sum = data[i][j]
        sum += data[i-1][j]
        sum += data[i+1][j]
        sum += data[i][j+1]
        sum += data[i][j-1]
        sum /= 5
    datarow.append(sum)
    processed_data.append(datarow)

matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
matplotlib.pyplot.imshow(processed_data)
matplotlib.pyplot.show()

# End ---------------------------------------
# Blur.
for i in (range(1,98)):
    datarow = []
    for j in (range(1,98)):
        
        # Move agent.
        if random.random() < 0.5:
            agents[i][0] += 1
        else:
            agents[i][0] -= 1
# Check if off edge and adjust.
if agents[i][0] < 0:
    agents[i][0] = 0
if agents[i][1] < 0:
    agents[i][0] = 0
if agents[i][0] > 99:
    agents[i][0] = 99
if agents[i][1] > 99:
    agents[i][0] = 99
print (agents)




 















