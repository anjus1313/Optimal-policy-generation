# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:23:56 2023

@author: Anju S
"""
from typing import List

from numpy.random import choice
import matplotlib.pyplot as plt

d0 = [0,1,2]                        #Initial state and their probabilities
d0_prob = [0.6,0.3,0.1]

pi = [0,1]                          #Actions (policy) and their probabilities
pi_prob = [[0.5,0.5],[0.7,0.3],[0.9,0.1],[0.4,0.6],[0.2,0.8]]

p = [3,4,5,6]                       #Transition states and their probabilities
p_prob = [[[1,0,0,0],[1,0,0,0]],[[0.8,0.2,0,0],[0.6,0.4,0,0]], \
          [[0.9,0.1,0,0],[0,1,0,0]],[[0,0,1,0],[0,0,0.3,0.7]],[[0,0,0.3,0.7],[0,0,0,1]]]


R = [[7,10],[-3,5],[4,-6],[9,-1],[-8,2]] #Rewards for different (state, action) pairs

gamma = 0.9                        #Discount
iterations = 150000

J = [0]*iterations                    #List of discounted return of each episode
J_hat: list[int] = [0]*(iterations+1) #List of average discounted return till episode i

def runEpisode(pi_prob, gamma):      #Returns the discounted return
    J_i = 0
    state = choice(d0,p=d0_prob)
    g_pow = 0
    while (state != 5 and state != 6):
        action = choice(pi,p=pi_prob[state])
        J_i += R[state][action]*(gamma**g_pow)
        g_pow += 1
        #print("s",state,"a", action, "reward", J_i)
        state = choice(p,p=p_prob[state][action])
    return J_i

for i in range(iterations):
    J[i] = runEpisode(pi_prob,gamma)
    #print("reward for episode",i,":", J)
    J_hat[i+1] = J_hat[i] + (J[i]-J_hat[i])/(i+1)

J_hat = J_hat[1:]

#print("average", sum(J)/iterations)

# Calculate variance of discounted returns
var = 0
for i in range(iterations):
    var += (J[i]-J_hat[-1])**2
var = var/(iterations-1)

#Plotting
episodes = range(iterations)
plt.plot(episodes, J_hat)
plt.title('Average discounted return till that episode, $\hat J(\pi$)')
plt.xlabel('Episodes')
plt.ylabel('$\hat J(\pi)$')
plt.show()

print("Average discounted return: ",J_hat[-1], "variance=",var)