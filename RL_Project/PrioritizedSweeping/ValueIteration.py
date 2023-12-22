import gym
from numpy.random import choice
import numpy as np

def makeCopy(V):
    copy = np.ones((32,11,2))*0
    for i in range(32):
        for j in range(11):
            for k in range(2):
                copy[i][j][k] = V[i][j][k]
    return copy

def LearnModel():
    iteration = 0
    while iteration < maxIterations:
        iteration += 1
        state = list(env.reset()[0])
        state[2] = int(state[2])
        done = False

        while not done:
            action = choice([0,1],p=[0.5,0.5])

            if tuple(state + [action]) in Count:
                Count[tuple(state + [action])] += 1
            else:
                Count[tuple(state + [action])] = 1

            next_state, reward, done, _, _ = env.step(action)
            next_state = list(next_state)
            next_state[2] = int(next_state[2])

            if tuple(state + [action] + next_state) in Model:
                Model[tuple(state + [action] + next_state)] += 1
            else:
                Model[tuple(state + [action] + next_state)] = 1

            state = next_state


env = gym.make("Blackjack-v1", sab=True)

maxIterations = 1000000
maxValueIterations = 1000
Model = {}
Count = {}
LearnModel()


p = {}

for key in Model:
    p[key] = Model[key]/Count[tuple(key[:4])]

gamma = 0.9
valueFunction = np.ones((32,11,2))*0

def ValueIteration():
    iteration = 0
    while(iteration < maxValueIterations):
        valueFunction_copy = makeCopy(valueFunction)


