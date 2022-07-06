import numpy
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
import pyswarms as ps

fruits = [[-1, 2, 3, -1, -1, 0, -1, -1, -1, -1],
          [-1, -1, -1, -1, 3, -1, 2, -1, -1, 6],
          [-1, -1, 5, -1, 5, 3, -1, 5, 7, 4],
          [-1, 4, -1, 5, -1, 5, -1, 6, -1, 3],
          [-1, -1, 4, -1, 5, -1, 6, -1, -1, 3],
          [-1, -1, -1, 2, -1, 5, -1, -1, -1, -1],
          [4, -1, 1, -1, -1, -1, 1, 1, -1, -1],
          [4, -1, 1, -1, -1, -1, 1, -1, 4, -1],
          [-1, -1, -1, -1, 6, -1, -1, -1, -1, 4],
          [-1, 4, 4, -1, -1, -1, -1, 4, -1, -1]]

options = {'c1': 0.2, 'c2': 0.1, 'w':1, 'k':2, 'p':1}

def f(x):
    n_particles = x.shape[0]
    j = [fitness_func(x[i]) for i in range(n_particles)]
    return numpy.array(j)

def fitness_func(solution):
    # print(solution)

    x = 0
    y = 0
    punish = 0

    # X=0,Y=0|X=0,Y=9|X=9,Y=0|X=9,Y=9|X=0,0<Y<9|X=9,0<Y<9|Y=0,0<X<9|Y=9,0<X<9|
    for k in range(len(solution)):
        pos = fruits[x][y]
        if pos >= 0:
            if x == 0 and y == 0:
                counter = 0
                for i in range(x, x + 2):
                    for j in range(y, y + 2):
                        if solution[i * 10 + j] == 1:
                            counter += 1
                punish += numpy.abs(pos - counter)
                y += 1
                # czy krawedz y
            if x == 0 and y == 9:
                counter = 0
                for i in range(x, x + 2):
                    for j in range(y - 1, y + 1):
                        if solution[i * 10 + j] == 1:
                            counter += 1
                punish += numpy.abs(pos - counter)
                x += 1
                y = 0
            if x == 9 and y == 0:
                counter = 0
                for i in range(x - 1, x + 1):
                    for j in range(y, y + 2):
                        if solution[i * 10 + j] == 1:
                            counter += 1
                punish += numpy.abs(pos - counter)
                y += 1
            if x == 0 and 0 < y < 9:
                counter = 0
                for i in range(x, x + 2):
                    for j in range(y - 1, y + 2):
                        if solution[i * 10 + j] == 1:
                            counter += 1
                punish += numpy.abs(pos - counter)
                y += 1
            if x == 9 and 0 < y < 9:
                counter = 0
                for i in range(x - 1, x + 1):
                    for j in range(y - 1, y + 2):
                        if solution[i * 10 + j] == 1:
                            counter += 1
                punish += numpy.abs(pos - counter)
                y += 1
            if y == 0 and 0 < x < 9:
                counter = 0
                for i in range(x - 1, x + 2):
                    for j in range(y, y + 2):
                        if solution[i * 10 + j] == 1:
                            counter += 1
                punish += numpy.abs(pos - counter)
                y += 1
            if y == 9 and 0 < x < 9:
                counter = 0
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 1):
                        if solution[i * 10 + j] == 1:
                            counter += 1
                punish += numpy.abs(pos - counter)
                x += 1
                y = 0
            if x == 9 and y == 9:
                counter = 0
                for i in range(x - 1, x + 1):
                    for j in range(y - 1, y + 1):
                        if solution[i * 10 + j] == 1:
                            counter += 1
                punish += numpy.abs(pos - counter)
                break
                # koniec
            if (9 > x > 0 and 9 > y > 0):
                counter = 0
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if solution[i * 10 + j] == 1:
                            counter += 1
                punish += numpy.abs(pos - counter)
                y += 1
        else:
            if y == 9:
                if x == 9:
                    break
                else:
                    x += 1
                    y = 0
            else:
                y += 1

    fitness = (numpy.abs(punish))
    return fitness

optimizer = ps.discrete.BinaryPSO(n_particles=100, dimensions=100,
options=options)
optimizer.optimize(f, iters=5000, verbose=True)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()

# 2022-04-20 13:43:19,197 - pyswarms.discrete.binary - INFO - Optimize for 2000 iters with {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 1, 'p': 1}
# pyswarms.discrete.binary: 100%|██████████|2000/2000, best_cost=20
# 2022-04-20 13:43:49,028 - pyswarms.discrete.binary - INFO - Optimization finished | best cost: 20.0, best pos: [1 0 0 1 1 0 0 1 1 1 1 0 0 1 0 1 0 1 0 1 1 1 1 1 0 0 0 0 1 1 0 0 0 1 0 1 1
#  1 1 0 0 0 1 0 1 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 1 0 0 0 1 0 0 0 0 1 1 0 0 0
#  0 0 0 0 0 0 1 1 0 1 1 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1]

# 2022-04-20 13:44:22,729 - pyswarms.discrete.binary - INFO - Optimize for 2000 iters with {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 2, 'p': 1}
# pyswarms.discrete.binary: 100%|██████████|2000/2000, best_cost=24
# 2022-04-20 13:44:54,182 - pyswarms.discrete.binary - INFO - Optimization finished | best cost: 24.0, best pos: [0 0 1 0 0 0 1 0 1 1 0 0 1 1 1 0 0 1 0 1 1 1 0 0 1 0 0 1 1 1 0 0 1 0 1 0 0
#  1 1 0 1 0 0 1 1 1 1 1 0 0 1 0 0 1 0 0 0 1 1 1 1 0 0 0 1 0 1 0 0 0 0 1 0 0
#  1 1 0 0 0 0 1 1 0 0 1 0 0 1 1 1 1 1 1 1 1 1 0 0 1 0]

# 2022-04-20 13:46:49,032 - pyswarms.discrete.binary - INFO - Optimize for 2000 iters with {'c1': 0.7, 'c2': 0.4, 'w': 0.9, 'k': 2, 'p': 1}
# pyswarms.discrete.binary: 100%|██████████|2000/2000, best_cost=21
# 2022-04-20 13:47:20,325 - pyswarms.discrete.binary - INFO - Optimization finished | best cost: 21.0, best pos: [0 0 1 0 0 0 0 1 1 1 0 0 1 1 0 0 0 0 1 1 1 0 0 1 1 0 0 1 1 0 0 1 1 1 1 0 1
#  0 1 0 1 0 0 0 0 1 1 0 1 0 0 0 1 0 0 1 1 0 0 1 1 0 0 0 0 0 1 0 0 0 1 0 0 1
#  1 0 0 0 1 1 1 1 0 0 1 0 1 0 1 0 0 0 1 1 0 1 1 0 1 0]

# 2022-04-20 13:48:42,505 - pyswarms.discrete.binary - INFO - Optimize for 2000 iters with {'c1': 0.5, 'c2': 0.3, 'w': 1, 'k': 2, 'p': 1}
# pyswarms.discrete.binary: 100%|██████████|2000/2000, best_cost=5
# 2022-04-20 13:49:12,846 - pyswarms.discrete.binary - INFO - Optimization finished | best cost: 5.0, best pos: [0 0 0 1 0 0 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1 0 1 0 1 0 0 1 1 1 0 0 1 1 1 1 0
#  1 0 0 0 0 1 0 0 1 1 1 0 1 1 1 0 0 0 1 0 0 1 1 1 0 0 0 1 0 0 0 0 1 1 0 0 0
#  1 0 0 0 1 1 1 1 0 1 1 0 1 0 0 1 1 1 0 1 1 1 1 1 1 0]

# 2022-04-20 13:50:14,863 - pyswarms.discrete.binary - INFO - Optimize for 2000 iters with {'c1': 0.4, 'c2': 0.2, 'w': 1, 'k': 2, 'p': 1}
# pyswarms.discrete.binary: 100%|██████████|2000/2000, best_cost=4
# 2022-04-20 13:50:47,041 - pyswarms.discrete.binary - INFO - Optimization finished | best cost: 4.0, best pos: [0 0 1 0 0 0 0 0 1 1 1 0 0 1 1 0 0 1 1 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1
#  1 1 0 1 0 0 0 1 1 1 1 0 1 1 1 0 0 1 0 1 0 0 1 1 0 0 0 0 0 0 0 0 1 1 0 0 0
#  1 0 0 0 0 1 1 1 0 0 1 1 0 0 1 1 0 1 1 1 1 1 1 1 1 0]

# 2022-04-20 13:55:32,542 - pyswarms.discrete.binary - INFO - Optimize for 5000 iters with {'c1': 0.2, 'c2': 0.1, 'w': 1, 'k': 2, 'p': 1}
# pyswarms.discrete.binary: 100%|██████████|5000/5000, best_cost=3
# 2022-04-20 13:56:57,647 - pyswarms.discrete.binary - INFO - Optimization finished | best cost: 3.0, best pos: [0 1 1 0 0 0 0 0 1 1 0 0 0 1 0 0 0 1 1 1 1 0 1 1 0 1 0 0 1 1 0 1 1 1 1 0 1
#  1 0 0 0 0 0 0 0 1 1 1 1 0 1 1 0 0 1 1 0 0 1 1 1 0 0 0 1 0 0 0 0 0 1 0 0 0
#  1 0 0 0 0 1 1 1 0 0 1 0 0 1 1 1 0 1 1 1 1 1 0 1 1 0]
