import numpy as np
from numpy.random import choice
import math

actions = [0, 1, 2, 3]  # [up,right,down,left]
optimalPolicy = [1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 0, 0, -1, 2, 2, 0, 0, -1, 2, 2, 0, 0, 1, 1, -1]
optimalValueFunction = [4.0187,4.5548,5.1575,5.8336,6.4553,4.3716,5.0324,5.8013,6.6473,7.3907,3.8672,4.3900,0,7.5769,8.4637,3.4182,3.8319,0,8.5738,9.6946,2.9977,2.9309,6.0733,9.6946,0]
alpha = 0.1
gamma = 0.9
delta = 0.001
maxIterations = 50
valueFunction = [0] * 25
valueFunction[12] = 0
valueFunction[17] = 0
valueFunction[24] = 0
d0 = [1 / 22] * 25
d0[12] = 0
d0[17] = 0
d0[24] = 0

R = [0] * 25
R[22] = -10
R[24] = 10


def initialState():
    return choice(list(range(25)), p=d0)


def ifValidState(state):
    if state < 0 or state > 24 or state == 12 or state == 17:
        return 0
    else:
        return 1


def nextState(state, action):
    pi = [0]*4
    if action == 0:
        if ifValidState(state-5):
            pi[0] = 0.8
        if state%5!=0:
            pi[1] = 0.05
        if (state+1)%5!=0:
            pi[2] = 0.05
        pi[3] = 1 - sum(pi)
        s = choice([state - 5, state - 1, state + 1, state], p=pi)
    if action == 1:
        if ifValidState(state+5):
            pi[1] = 0.05
        if ifValidState(state-5):
            pi[2] = 0.05
        if (state+1)%5!=0:
            pi[0] = 0.8
        pi[3] = 1 - sum(pi)
        s = choice([state + 1, state + 5, state - 5, state], p=pi)
    if action == 2:
        if ifValidState(state+5):
            pi[0] = 0.8
        if state%5!=0:
            pi[1] = 0.05
        if (state+1)%5!=0:
            pi[2] = 0.05
        pi[3] = 1 - sum(pi)
        s = choice([state + 5, state - 1, state + 1, state], p=pi)
    if action == 3:
        if ifValidState(state+5):
            pi[1] = 0.05
        if ifValidState(state-5):
            pi[2] = 0.05
        if state%5!=0:
            pi[0] = 0.8
        pi[3] = 1 - sum(pi)
        s = choice([state - 1, state + 5, state - 5, state], p=pi)
    if ifValidState(s):
        return s
    else:
        return state


def print_valueFunction(valueFunction):
    valueFunctionCopy = [0] * 25
    for i in range(len(valueFunction)):
        valueFunctionCopy[i] = round(valueFunction[i], 4)
    valueFunctionMatrix = np.array(
        [valueFunctionCopy[0:5], valueFunctionCopy[5:10], valueFunctionCopy[10:15], valueFunctionCopy[15:20],
         valueFunctionCopy[20:25]])
    print("Value Function\n", valueFunctionMatrix)


def maxNorm(newValue, value):
    max_norm = 0
    for i in range(len(value)):
        if abs(newValue[i] - value[i]) > max_norm:
            max_norm = abs(newValue[i] - value[i])
    return max_norm


def makeCopy(value):
    valueCopy = [0] * 25
    for i in range(len(value)):
        valueCopy[i] = value[i]
    return valueCopy


def runAlgorithm():
    max_norm = 10
    episode = 0
    while (max_norm > delta):
        oldValueFunction = makeCopy(valueFunction)
        episode += 1
        state = initialState()
        while (state != 24):
            action = optimalPolicy[state]
            next_state = nextState(state, action)
            r = R[next_state]
            valueFunction[state] += alpha * (r + gamma * valueFunction[next_state] - valueFunction[state])
            state = next_state

        max_norm = maxNorm(oldValueFunction, valueFunction)
    print(episode)
    return [valueFunction,episode]


Avg_valueFunction = [0]*25
Episodes = []
for i in range(maxIterations):
    runAlgorithmRet = runAlgorithm()
    Avg_valueFunction = [(a + b) for a, b in zip(runAlgorithmRet[0], Avg_valueFunction)]
    Episodes.append(runAlgorithmRet[1])

for j in range(25):
    Avg_valueFunction[j] /= maxIterations

print("Average")
print_valueFunction(Avg_valueFunction)
print("max norm",maxNorm(Avg_valueFunction,optimalValueFunction))

std_dev = 0
for i in range(len(Episodes)):
    std_dev += (Episodes[i]-sum(Episodes)/maxIterations)**2
std_dev = math.sqrt(std_dev/(len(Episodes)-1))


print("Average number of episodes : ",sum(Episodes)/maxIterations)
print("Standard deviation : ",std_dev)