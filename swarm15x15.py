import numpy
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
import pyswarms as ps

fruits = [[2, -1, 3, -1, 3, -1, 3, -1, 4, 5, 5, 4, -1, -1, 0],
        [-1, -1, -1, 3, -1, 4, -1, 4, -1, -1, -1, -1, -1, -1, -1],
        [1, -1, 2, 1, 2, 2, 3, 2, 2, 2, -1, -1, 4, 3, -1],
        [-1, -1, 3, -1, 3, -1, -3, -1, 0, -1, -1, -1, -1, 4, -1],
        [-1, -1, -1, -1, -1, -1, 3, -1, -1, -1, -1, 5, 7, -1, -1],
        [5, -1, -1, 7, -1, 6, -1, -1, -1, 2, -1, -1, -1, -1, -1],
        [-1, -1, 5, -1, 7, 5, 5, 3, -1, -1, -1, -1, 5, 4, 1],
        [5, -1, -1, 7, -1, 7, -1, -1, -1, -1, -1, 7, -1, -1, -1],
        [-1, -1, 7, -1, -1, 8, 9, -1, -1, 9, -1, -1, 9, 6, -1],
        [5, -1, 7, -1, 8, -1, 7, -1, 9, -1, -1, -1, 8, 7, -1],
        [4, -1, -1, -1, 6, -1, -1, -1, 6, 6, -1, -1, -1, 7, 5],
        [-1, -1, 6, -1, -1, 5, 6, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 8, 7, -1, -1, 7, -1, 5, -1, 5, 8, 8, -1, -1, 4],
        [-1, 8, 7, -1, -1, -1, -1, -1, 4, -1, 8, -1, 5, -1, 2],
        [-1, -1, -1, -1, 3, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1]]

options = {'c1': 0.2, 'c2': 0.1, 'w':1, 'k':15, 'p':1}

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
        
            

    fitness = (numpy.abs(punish))
    return fitness

optimizer = ps.discrete.BinaryPSO(n_particles=len(fruits[0])*len(fruits[0]), dimensions=len(fruits[0])*len(fruits[0]),
options=options)
optimizer.optimize(f, iters=4000, verbose=True)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()

# 2022-04-24 14:43:50,412 - Optimize for 2000 iters with {'c1': 0.2, 'c2': 0.1, 'w': 1, 'k': 9, 'p': 1}
# 2022-04-24 14:48:38,125 - Optimization finished | best cost: 21.0, best pos: [0 1 0 1 1 0 1 1 1 1 1 1 1 0 0 0 0 0 1 0 0 1 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0
#  0 0 1 0 0 1 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 1 1 1 1 0 1 1 0 1 0 0 0 0 1 0 1
#  0 1 0 1 1 1 1 0 0 0 0 1 1 1 0 1 1 0 0 1 1 0 1 0 0 1 0 0 1 0 0 1 1 0 1 0 1
#  1 1 1 1 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1
#  1 1 0 1 0 0 0 1 0 1 1 1 0 1 0 1 0 1 0 1 1 0 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1
#  0 1 0 0 1 1 1 1 0 1 1 1 1 0 1 1 1 1 0 1 1 1 0 1 0 1 1 0 1 0 0 1 1 0 0 1 1
#  0 0 0]