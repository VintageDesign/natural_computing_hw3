import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import random
import math

#Function for Both SA and Hill Climb
def evaluate(x):
    y = float((x - .1)/.9)
    y = math.pow(y, 2.0)
    y = math.pow(2.0,(-2.0 * y) )
    y = y * math.pow(math.sin(5*math.pi*x), 6)
    return y;

# A perturbation is a city swap
def swap():
    x = random.random()
    return x


def accept_solution(energy1, energy2, temperature):
    if energy1 < energy2:
        return True
    else:
        a = math.exp((energy2 - energy1) / temperature)
        b = random.random()
        if a > b:
            return True
        else:
            return False

def main(start_x, temperature , cooling_factor = .01):
    start_y = evaluate(start_x)
    i = 0
    iterations = []
    while temperature > 0.01:
        new_x = swap()
        new_y = evaluate(new_x)
        if accept_solution(start_y, new_y, temperature):
            start_x = new_x
            start_y = new_y

        temperature *= 1 - cooling_factor
#        if (i%50==0):  plot([start_x, start_y],path = 1, wait = 0)
        i = i+1
        iterations.append(start_x)
    print start_x
    return iterations


def plot(point, path, wait):
    plt.clf()
    if (path == 1):
        plt.plot(point[0], point[1], color='red', zorder=0, label='Approximate')
        plt.plot(.1, evaluate(.1),color='blue', label='Actual')
    plt.scatter(point[0], point[1], marker='o')
    plt.scatter(.1, evaluate(.1),marker='^')
    plt.xlim(-.1,1.1)
    plt.ylim(-.5,1.5)
    plt.axis('on')
    if (wait == 0):  plt.ion()
    leg = plt.legend()
    plt.show()
    plt.pause(.001)

start_x = random.uniform(0,1)
#max_x = optimize.fmin(lambda x: -evaluate(x), 0)
final =  main(start_x, temperature = 35)
plt.ioff()
#print "Done"
f_range = np.arange(0, len(final), 1)
plt.clf()
plt.plot(f_range, final, 'ro', label='Approximation', markersize=1)
plt.plot(f_range,[.1]*len(final), 'b--',label='Actual', markersize=.5)
plt.xlabel("Iteration")
plt.ylabel("Input Value")
leg = plt.legend()

#plt.show()
