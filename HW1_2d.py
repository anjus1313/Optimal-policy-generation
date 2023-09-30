# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:23:56 2023

@author: Anju S
"""
import math
from typing import List

from numpy.random import choice
import matplotlib.pyplot as plt


d0 = [0,1,2]                        #Initial state and their probabilities
d0_prob = [0.6,0.3,0.1]

pi = [0,1]                          #Actions (policy) and their probabilities
pi_prob = [[0.5,0.5],[0.7,0.3],[0.9,0.1],[0.4,0.6],[0.2,0.8]]

p = [3,4,5,6]                       #Transition states (s')
p_prob = [[[1,0,0,0],[1,0,0,0]],[[0.8,0.2,0,0],[0.6,0.4,0,0]], \
          [[0.9,0.1,0,0],[0,1,0,0]],[[0,0,1,0],[0,0,0.3,0.7]],[[0,0,0.3,0.7],[0,0,0,1]]] #p(s,a,s') for 5 states and 2 actions

R = [[7,10],[-3,5],[4,-6],[9,-1],[-8,2]] #Rewards for different (state, action) pairs

gamma = 0.9                         #Discount
iterations = 100                    #No of episodes

J = [0]*iterations                  #List of discounted returns of episodes
J_hat: list[int] = [0]*(260+1)      #List of average discounted return till episode i


#Returns the discounted return
def runEpisode(pi_prob, gamma):
    discountReturn = 0
    state = choice(d0,p=d0_prob)
    gPower = 0
    while (state != 5 and state != 6):
        action = choice(pi,p=pi_prob[state])
        discountReturn += R[state][action]*(gamma**gPower)
        gPower += 1
        #print("s",state,"a", action, "reward", discountReturn)
        state = choice(p,p=p_prob[state][action])
    return discountReturn

#Returns the expected discounted return
def find_J_pi(pi_prob):
    for i in range(iterations):
        J[i] = runEpisode(pi_prob,gamma)
        #print("reward for episode",i,":", J)
        #J_hat[i+1] = J_hat[i] + (J[i]-J_hat[i])/(i+1)
    #J_hat = J_hat[1:]
    return sum(J)/iterations

#Finds best policy performance among n random policies
for n in range(1,261,10):
    perf = -100
    for i in range(n):
        for j in range(len(pi_prob)):
            pi_prob[j][0] = choice([0,1],p=[0.5,0.5])
            pi_prob[j][1] = 1-pi_prob[j][0]
        J_pi = find_J_pi(pi_prob)
        if J_pi > perf:
            perf = J_pi
    #print(perf)
    J_hat[n] = perf

#Plotting
episodes = range(1,261,10)
plt.plot(episodes, [J_hat[x] for x in episodes])
plt.title('Best policy performance (Empirical way)')
plt.xlabel('N')
plt.ylabel('$\hat J(\pi)$')
plt.ylim(0,20)
plt.grid(which='both')
plt.minorticks_on()
plt.show()
