import numpy as np
np.set_printoptions(precision=4, suppress=True)
valueFunction = np.zeros((5,5))

theta = 0.0001
actions = [0,1,2,3] #[up,right,down,left]
R = np.zeros((5,5))
R[4][4] = 10
R[4][2] = -10
#R[0][2] = 5
gamma = 0.9
def ifValidState(r,c):
    if r<0 or c<0 or r>4 or c>4 or (r==2 and c==2) or (r==3 and c==2):
        return 0
    else:
        return 1

def isTerminal(r,c):
    if (r==4 and c==4): #or (r==0 and c==2):
        return 1
    else: return 0
def find_q_s(r, c, valueFunction):
    q_s = [0.0,0.0,0.0,0.0]
    for action in actions:
        p = {(r,c):0}
        if action == 0:
            if ifValidState(r-1,c): p[(r-1,c)] = 0.8
            else: p[(r,c)] += 0.8
            if ifValidState(r,c+1): p[(r,c+1)] = 0.05
            else: p[(r,c)] += 0.05
            if ifValidState(r,c-1): p[(r,c-1)] = 0.05
            else: p[(r,c)] += 0.05
            p[(r,c)] += 0.1
        if action == 1:
            if ifValidState(r,c+1): p[(r,c+1)] = 0.8
            else: p[(r,c)] += 0.8
            if ifValidState(r-1,c): p[(r-1,c)] = 0.05
            else: p[(r,c)] += 0.05
            if ifValidState(r+1,c): p[(r+1,c)] = 0.05
            else: p[(r,c)] += 0.05
            p[(r,c)] += 0.1
        if action == 2:
            if ifValidState(r+1,c): p[(r+1,c)] = 0.8
            else: p[(r,c)] += 0.8
            if ifValidState(r,c+1): p[(r,c+1)] = 0.05
            else: p[(r,c)] += 0.05
            if ifValidState(r,c-1): p[(r,c-1)] = 0.05
            else: p[(r,c)] += 0.05
            p[(r,c)] += 0.1
        if action == 3:
            if ifValidState(r,c-1): p[(r,c-1)] = 0.8
            else: p[(r,c)] += 0.8
            if ifValidState(r-1,c): p[(r-1,c)] = 0.05
            else: p[(r,c)] += 0.05
            if ifValidState(r+1,c): p[(r+1,c)] = 0.05
            else: p[(r,c)] += 0.05
            p[(r,c)] += 0.1
        #print("r,c",r,c,"action",action,"p",p)
        for (row,col) in p:
            q_s[action] += p[(row,col)]*(R[row][col]+gamma*valueFunction[row][col])
        #print("q_s",q_s)
    return q_s
def getMaxReturn(r,c,valueFunction):
    if isTerminal(r,c):
        return 0
    q_s = find_q_s(r,c, valueFunction)
    return max(q_s)

def getOptimalValue(valueFunction):
    Delta = 1
    i = 0
    while(Delta>=theta):
        Delta = 0
        valueFunctionCopy = np.zeros((5,5))
        for r in range(len(valueFunction)):
            for c in range(len(valueFunction[0])):
                valueFunctionCopy[r][c] = valueFunction[r][c]
        for r in range(len(valueFunction)):
            for c in range(len(valueFunction[0])):
                if (r==2 and c==2) or (r==3 and c==2):
                    valueFunction[r][c] = 0
                else:
                    new_value = getMaxReturn(r,c,valueFunctionCopy)
                    Delta = max(Delta,abs(valueFunction[r][c]-new_value))
                    valueFunction[r][c] = new_value
        i += 1
    print("Iterations",i)
    return valueFunction

Policy = -1*np.ones((5,5))
optValueFunction = getOptimalValue(valueFunction)
for r in range(len(Policy)):
    for c in range(len(Policy[0])):
        if not ((r==2 and c==2) or (r==3 and c==2)):
            q_s = find_q_s(r,c,optValueFunction)
            Policy[r][c] = q_s.index(max(q_s))


Policy_symbol = [[], [], [], [], []]
for r in range(len(Policy)):
    for c in range(len(Policy[0])):
        if Policy[r][c]==-1: Policy_symbol[r].append(" ")
        if Policy[r][c]==0: Policy_symbol[r].append("\u2191")
        if Policy[r][c]==1: Policy_symbol[r].append("\u2192")
        if Policy[r][c]==2: Policy_symbol[r].append("\u2193")
        if Policy[r][c]==3: Policy_symbol[r].append("\u2190")
Policy_symbol[4][4] = "G"
#Policy_symbol[0][2] = "g"
print("Final value function","\n",optValueFunction)
print("Final policy")
for r in range(len(Policy)):
    for c in range(len(Policy[0])):
        print(Policy_symbol[r][c], end="\t")
    print()
