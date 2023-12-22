import numpy as np
from numpy.random import choice

optimalValueFunction = [4.0187,4.5548,5.1575,5.8336,6.4553,4.3716,5.0324,5.8013,6.6473,7.3907,3.8672,4.3900,0,7.5769,8.4637,3.4182,3.8319,0,8.5738,9.6946,2.9977,2.9309,6.0733,9.6946,0]

actions = [0, 1, 2, 3]  # [up,right,down,left]

alpha = 0.1
gamma = 0.9
maxIterations = 2000

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

def Policy(state, epsilon):
    pi = [0,0,0,0]
    maximum_q = max(q_s_a[state])
    numberOfMax = 0
    for a in range(len(q_s_a[state])):
        if q_s_a[state][a] == maximum_q:
            numberOfMax += 1
    for a in range(len(q_s_a[state])):
        if q_s_a[state][a] == maximum_q:
            pi[a] = (1-epsilon)/numberOfMax + epsilon/len(q_s_a[state])
        else:
            pi[a] = epsilon/len(q_s_a[state])

    return pi

def calculate_valueFunction(q, pi):
    value = [0]*25
    for s in range(len(q)):
        for a in range(len(actions)):
            value[s] += pi[s][a]*q_s_a[s][a]

    return value
def print_valueFunction(valueFunction):

    valueFunctionMatrix = np.array([valueFunction[0:5], valueFunction[5:10], valueFunction[10:15], valueFunction[15:20],
                                    valueFunction[20:25]])
    for i in range(len(valueFunctionMatrix)):
        for j in range(len(valueFunctionMatrix[0])):
            valueFunctionMatrix[i][j] = round(valueFunctionMatrix[i][j], 4)
    print("Value Function\n", valueFunctionMatrix)


def runEpisode(q_s_a,epsilon):
    state = initialState()

    while(state!=24):
        action = choice(actions,p=Policy(state, epsilon))
        next_state = nextState(state, action)
        r = R[next_state]
        q_s_a[state, action] += alpha * (r + gamma * max(q_s_a[next_state]) - q_s_a[state, action])
        state = next_state

def runAlgorithm(q_s_a):
    iteration = 0
    epsilon_high = 1
    epsilon_low = 0
    epsilon = epsilon_high
    while(iteration < maxIterations):
        iteration += 1
        epsilon = epsilon-(epsilon_high-epsilon_low)/2000
        runEpisode(q_s_a,epsilon)


q_s_a = np.ones((25,4))*10
q_s_a[12] = [0,0,0,0]
q_s_a[17] = [0,0,0,0]
q_s_a[24] = [0,0,0,0]
runAlgorithm(q_s_a)

print("Learned q function\n", q_s_a)

new_valueFunction = [0]*25
for s in range(len(q_s_a)):
    new_valueFunction[s] = max(q_s_a[s])
print_valueFunction(new_valueFunction)

Policy_symbol = []
for i in range(len(q_s_a)):
    if np.argmax(q_s_a[i]) == 0: Policy_symbol.append("\u2191")
    if np.argmax(q_s_a[i]) == 1: Policy_symbol.append("\u2192")
    if np.argmax(q_s_a[i]) == 2: Policy_symbol.append("\u2193")
    if np.argmax(q_s_a[i]) == 3: Policy_symbol.append("\u2190")
Policy_symbol[12] = " "
Policy_symbol[17] = " "
Policy_symbol[24] = "G"

print("Policy learned")
for i in range(len(Policy_symbol)):
    if i%5==0:
        print(end="\n")
    print(Policy_symbol[i], end="\t")


