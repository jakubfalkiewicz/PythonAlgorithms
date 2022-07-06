import numpy
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
import pyswarms as ps

fruits = [[-1,5,4,-1,-1],
          [-1,-1,-1,-1,3],
          [-1,5,6,-1,5],
          [0,2,5,-1,5],
          [-1,-1,-1,-1,-1]]

options = {'c1': 0.2, 'c2': 0.1, 'w':1, 'k':2, 'p':1}

def f(x):
    n_particles = x.shape[0]
    j = [fitness_func(x[i]) for i in range(n_particles)]
    return numpy.array(j)

def fitness_func(solution):
    
    x = 0
    y = 0
    punish = 0
    
    for k in range(len(solution)):
        pos = fruits[x][y]
        if pos>=0:
            if x == 0 and y == 0:
                counter=0
                for i in range(x,x+2):
                    for j in range(y,y+2):
                        if solution[i*len(fruits[0]) + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
                #czy krawedz y
            if x == 0 and y == len(fruits[0])-1:
                counter=0
                for i in range(x,x+2):
                    for j in range(y-1,y+1):
                        if solution[i*len(fruits[0]) + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                x+=1
                y=0
            if x == len(fruits[0])-1 and y == 0:
                counter=0
                for i in range(x-1,x+1):
                    for j in range(y,y+2):
                        if solution[i*len(fruits[0]) + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
            if x == 0 and 0<y<len(fruits[0])-1:
                counter=0
                for i in range(x,x+2):
                    for j in range(y-1,y+2):
                        if solution[i*len(fruits[0]) + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
            if x == len(fruits[0])-1 and 0<y<len(fruits[0])-1:
                counter=0
                for i in range(x-1,x+1):
                    for j in range(y-1,y+2):
                        if solution[i*len(fruits[0]) + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
            if y == 0 and 0<x<len(fruits[0])-1:
                counter=0
                for i in range(x-1,x+2):
                    for j in range(y,y+2):
                        if solution[i*len(fruits[0]) + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
            if y == len(fruits[0])-1 and 0<x<len(fruits[0])-1:
                counter=0
                for i in range(x-1,x+2):
                    for j in range(y-1,y+1):
                        if solution[i*len(fruits[0]) + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                x+=1
                y=0
            if x == len(fruits[0])-1 and y == len(fruits[0])-1:
                counter=0
                for i in range(x-1,x+1):
                    for j in range(y-1,y+1):
                        if solution[i*len(fruits[0]) + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                break
                #koniec
            if (len(fruits[0])-1>x>0 and len(fruits[0])-1>y>0):
                counter=0
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if solution[i*len(fruits[0]) + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
        else:
            if y==len(fruits[0])-1:
                if x==len(fruits[0])-1:
                    break
                else:
                    x+=1
                    y=0
            else:
                y+=1
        
            

    fitness = (numpy.abs(punish)-2)
    return fitness

optimizer = ps.discrete.BinaryPSO(n_particles=25, dimensions=25,
options=options)
optimizer.optimize(f, iters=125, verbose=True)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()

# 2022-04-22 22:14:57,151 - Optimize for 125 iters with {'c1': 0.2, 'c2': 0.1, 'w': 1, 'k': 2, 'p': 1}
# 2022-04-22 22:14:57,467 - Optimization finished | best cost: 0.0, best pos: [0 1 1 0 0 1 1 1 0 1 0 0 1 1 1 0 0 1 1 1 0 0 0 1 0]

# 2022-04-23 00:04:18,596 - Optimize for 125 iters with {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 2, 'p': 1}
# 2022-04-23 00:04:18,899 - Optimization finished | best cost: 2.0, best pos: [1 0 1 0 0 1 1 1 1 0 0 0 0 1 1 1 0 1 1 1 0 0 0 1 0]