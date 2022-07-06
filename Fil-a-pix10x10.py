import pygad
import numpy
import matplotlib.pylab as plt
# from random import choice
import time

fruits = [[-1,2,3,-1,-1,0,-1,-1,-1,-1],
          [-1,-1,-1,-1,3,-1,2,-1,-1,6],
          [-1,-1,5,-1,5,3,-1,5,7,4],
          [-1,4,-1,5,-1,5,-1,6,-1,3],
          [-1,-1,4,-1,5,-1,6,-1,-1,3],
          [-1,-1,-1,2,-1,5,-1,-1,-1,-1],
          [4,-1,1,-1,-1,-1,1,1,-1,-1],
          [4,-1,1,-1,-1,-1,1,-1,4,-1],
          [-1,-1,-1,-1,6,-1,-1,-1,-1,4],
          [-1,4,4,-1,-1,-1,-1,4,-1,-1]]

solve = [[0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0, 0, 0, 1, 1, 1], 
         [0, 0, 1, 1, 1, 0, 0, 1, 1, 1], 
         [0, 1, 1, 0, 1, 1, 0, 1, 0, 0], 
         [0, 1, 0, 0, 0, 1, 1, 1, 1, 0], 
         [1, 1, 0, 0, 1, 1, 0, 0, 1, 1], 
         [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
         [1, 1, 0, 0, 1, 1, 0, 0, 1, 1], 
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

# definiujemy parametry chromosomu
# geny to liczby: 0 lub 1
gene_space = [0,1]


# definiujemy funkcjÄ fitness
def fitness_func(solution, solution_idx):

    # print(solution)
    
    x = 0
    y = 0
    punish = 0
    
    #X=0,Y=0|X=0,Y=9|X=9,Y=0|X=9,Y=9|X=0,0<Y<9|X=9,0<Y<9|Y=0,0<X<9|Y=9,0<X<9|
    for k in range(len(solution)):
        pos = fruits[x][y]
        if pos>=0:
            if x == 0 and y == 0:
                counter=0
                for i in range(x,x+2):
                    for j in range(y,y+2):
                        if solution[i*10 + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
                #czy krawedz y
            if x == 0 and y == 9:
                counter=0
                for i in range(x,x+2):
                    for j in range(y-1,y+1):
                        if solution[i*10 + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                x+=1
                y=0
            if x == 9 and y == 0:
                counter=0
                for i in range(x-1,x+1):
                    for j in range(y,y+2):
                        if solution[i*10 + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
            if x == 0 and 0<y<9:
                counter=0
                for i in range(x,x+2):
                    for j in range(y-1,y+2):
                        if solution[i*10 + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
            if x == 9 and 0<y<9:
                counter=0
                for i in range(x-1,x+1):
                    for j in range(y-1,y+2):
                        if solution[i*10 + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
            if y == 0 and 0<x<9:
                counter=0
                for i in range(x-1,x+2):
                    for j in range(y,y+2):
                        if solution[i*10 + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
            if y == 9 and 0<x<9:
                counter=0
                for i in range(x-1,x+2):
                    for j in range(y-1,y+1):
                        if solution[i*10 + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                x+=1
                y=0
            if x == 9 and y == 9:
                counter=0
                for i in range(x-1,x+1):
                    for j in range(y-1,y+1):
                        if solution[i*10 + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                break
                #koniec
            if (9>x>0 and 9>y>0):
                counter=0
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if solution[i*10 + j] == 1:
                            counter+=1
                punish+=numpy.abs(pos-counter)
                y+=1
        else:
            if y==9:
                if x==9:
                    break
                else:
                    x+=1
                    y=0
            else:
                y+=1
        
            

    fitness = -(numpy.abs(punish))
    return fitness


fitness_function = fitness_func

# ile chromsomĂłw w populacji
# ile genow ma chromosom
sol_per_pop = 200
num_genes = 100

# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 100
num_generations = 2000
keep_parents = 110

# jaki typ selekcji rodzicow?
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

# w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 2

# kryterium stopu
stop_criteria = "reach_0"

# inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=stop_criteria)

# uruchomienie algorytmu
start = time.time()
ga_instance.run()
end = time.time()
print(round(end - start, 3))

# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
res = numpy.array(solution,dtype=int)
result=[[],[],[],[],[],[],[],[],[],[]]
for i in range(len(res)):
    result[int(i/10)].append(res[i])

# tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
# prediction = numpy.sum(S*solution)
# print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

# wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()
fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(result, vmin=0, vmax=1,cmap=plt.cm.gray)
ax[0].set_title('Result')

ax[1].imshow(solve, vmin=0, vmax=1,cmap=plt.cm.gray)
ax[1].set_title('Original')

plt.show()
# 442.228
# Parameters of the best solution : [0. 1. 1. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 1. 0. 0. 0. 1. 1. 1. 0. 0. 1. 1.
#  1. 0. 0. 1. 1. 1. 0. 1. 1. 0. 1. 1. 0. 1. 0. 0. 0. 1. 0. 0. 0. 1. 1. 1.
#  1. 0. 1. 1. 0. 0. 1. 1. 0. 0. 1. 1. 1. 0. 0. 0. 1. 0. 0. 0. 0. 1. 1. 0.
#  0. 0. 1. 0. 0. 0. 0. 1. 1. 1. 0. 0. 1. 1. 0. 0. 1. 1. 0. 1. 1. 1. 1. 1.
#  1. 1. 1. 0.]
# Fitness value of the best solution = 0