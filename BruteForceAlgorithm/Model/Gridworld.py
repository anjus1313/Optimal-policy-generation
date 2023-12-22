# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:23:56 2023

@author: Anju S
"""

from numpy.random import choice
import matplotlib.pyplot as plt


d0 = [i for i in range(0,25)]                       #Initial state and their probabilities
d0_prob = [1]+[0]*24

actions = [0,1,2,3]                                 #Actions
pi = [0]*25
R = [0]*24+[100]
gamma = 0.9                                         #Discount

episodes = 50
J = [0]*episodes                  #List of discounted returns of episodes

#Get next state
def getNextState(state, action):
    states = [state+1,state-1,state+5,state-5,state]
    forbidden_actions = []
    for i in states:
        if i>-1 and i<25:
            forbidden_actions.append(1)
        else:
            forbidden_actions.append(0)

    if(action==0):
        #p = [0.8,0,0.05,0.05,0.1]
        p = [1,0,0,0,0]
        nextState_prob = [p[i]*forbidden_actions[i] for i in range(len(p))]
        nextState_prob[-1] = 1-sum(nextState_prob[:4])

    if(action==1):
        p = [0,0.8,0.05,0.05,0.1]
        p = [0,1,0,0,0]
        nextState_prob = [p[i]*forbidden_actions[i] for i in range(len(p))]
        nextState_prob[-1] = 1-sum(nextState_prob[:4])

    if(action==2):
        p = [0.05,0.05,0.8,0,0.1]
        p = [0,0,1,0,0]
        nextState_prob = [p[i]*forbidden_actions[i] for i in range(len(p))]
        nextState_prob[-1] = 1-sum(nextState_prob[:4])

    if(action==3):
        p = [0.05,0.05,0,0.8,0.1]
        p = [0,0,0,1,0]
        nextState_prob = [p[i]*forbidden_actions[i] for i in range(len(p))]
        nextState_prob[-1] = 1-sum(nextState_prob[:4])


    return choice(states, p = nextState_prob)


#Returns the discounted return
def runEpisode(pi, gamma):
    discountReturn = 0
    state = choice(d0,p=d0_prob)
    gPower = 0
    while (state != 24 and gPower != 50):
        action = pi[state]
        state = getNextState(state, action)
        discountReturn += R[state]*(gamma**gPower)
        gPower += 1
        #print("s",state,"a", action, "reward", discountReturn)

    return discountReturn

#Returns the expected discounted return
def find_J_pi(pi):
    for i in range(episodes):
        J[i] = runEpisode(pi,gamma)
        #print("reward for episode",i,":", J[i])
        #J_hat[i+1] = J_hat[i] + (J[i]-J_hat[i])/(i+1)
    #J_hat = J_hat[1:]
    return sum(J)/episodes

#Finds best policy performance among n random policies
#for n in range(1,101,10):
#perf = -100
def runIteration(pi_saved,perf):
    for i in range(10):
        for j in range(len(pi)):
            pi[j] = choice(actions,p=[0.25,0.25,0.25,0.25])

        J_pi = find_J_pi(pi)
        if J_pi > perf:
            perf = J_pi
            pi_saved = pi
    #print(perf)
    return [pi_saved,perf]


