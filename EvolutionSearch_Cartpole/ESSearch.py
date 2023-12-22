import math
import numpy as np
import random

x_range = np.array([-2.4,2.4])
v_range = np.array([-1.56427, 1.56427])
w_range = np.array([-math.pi/15, math.pi/15])
w_dot_range = np.array([-2.43909, 2.43909])

g = 9.8
m_c = 1.0
m_p = 0.1
m_t = m_c + m_p
l = 0.5
tou = 0.02
F = np.array([-10,10])
state = np.array([0.0,0.0,0.0,0.0])           #[x,v,angle,ang_vel]
actions = np.array([0,1])                     #[left, right]
R = 1
gamma = 1
time_steps = 50

def defineGuassian(n):
    global mean, cov_matrix
    mean = np.array([0]*n)
    cov_matrix = np.identity(n)

def getPerturbation(n):
    perturbation = np.array([])
    for i in range(n):
        perturbation = np.append(perturbation, random.gauss(mean[i], cov_matrix[i][i]))
    return perturbation

def normalizeStateCos(s):
    s[0] = (s[0]-min(x_range))/(max(x_range)-min(x_range))
    s[1] = (s[1]-min(v_range))/(max(v_range)-min(v_range))
    s[2] = (s[2]-min(w_range))/(max(w_range)-min(w_range))
    s[3] = (s[3]-min(w_dot_range))/(max(w_dot_range)-min(w_dot_range))
    return s

def normalizeStateSine(s):
    s[0] = 2*(s[0]-min(x_range))/(max(x_range)-min(x_range)) - 1
    s[1] = 2*(s[1]-min(v_range))/(max(v_range)-min(v_range)) - 1
    s[2] = 2*(s[2]-min(w_range))/(max(w_range)-min(w_range)) - 1
    s[3] = 2*(s[3]-min(w_dot_range))/(max(w_dot_range)-min(w_dot_range)) - 1
    return s
def getCosStateFeatureVector(state_norm, M):
    stateFeature_x, stateFeature_v, stateFeature_w, stateFeature_w_dot = np.array([]), np.array([]), np.array([]), np.array([])
    for m in range(1,M+1):
        stateFeature_x = np.append(stateFeature_x, math.cos(m*math.pi*state_norm[0]))
        stateFeature_v = np.append(stateFeature_v, math.cos(m*math.pi*state_norm[1]))
        stateFeature_w = np.append(stateFeature_w, math.cos(m*math.pi*state_norm[2]))
        stateFeature_w_dot = np.append(stateFeature_w_dot, math.cos(m*math.pi*state_norm[3]))
    return np.concatenate(([1],stateFeature_x,stateFeature_v,stateFeature_w,stateFeature_w_dot))    #Return state feature vector

def getSineStateFeatureVector(state_norm, M):
    stateFeature_x, stateFeature_v, stateFeature_w, stateFeature_w_dot = np.array([]), np.array([]), np.array([]), np.array([])
    for m in range(1,M+1):
        stateFeature_x = np.append(stateFeature_x, math.sin(m*math.pi*state_norm[0]))
        stateFeature_v = np.append(stateFeature_v, math.sin(m*math.pi*state_norm[1]))
        stateFeature_w = np.append(stateFeature_w, math.sin(m*math.pi*state_norm[2]))
        stateFeature_w_dot = np.append(stateFeature_w_dot, math.sin(m*math.pi*state_norm[3]))
    return np.concatenate(([1],stateFeature_x,stateFeature_v,stateFeature_w,stateFeature_w_dot))

def getAction(theta, state, M, stateFeature):
    state_copy = np.array([state[0],state[1],state[2],state[3]])
    if stateFeature=="Cos":
        state_norm = normalizeStateCos(state_copy)
    elif stateFeature=="Sine":
        state_norm = normalizeStateSine(state_copy)
    stateFeatureVector = np.transpose(getCosStateFeatureVector(state_norm,M).reshape(-1,1))
    theta = np.expand_dims(theta, axis=1)
    threshold = stateFeatureVector@theta
    if threshold <= 0:
        return 0
    else:
        return 1


def runEpisode(theta, M, stateFeature):
    state = np.array([0.0,0.0,0.0,0.0])
    step = 0
    G = 0
    g_pow = 0

    while((state[0] >= min(x_range) and state[0] <= max(x_range)) and (state[2] >= min(w_range) and state[2] <= max(w_range)) and step < 500):

        action = getAction(theta, state, M, stateFeature)

        b = (F[action] + m_p*l*(state[3]**2)*math.sin(state[2]))/m_t
        c = (g*math.sin(state[2])-math.cos(state[2])*b)/(l*(4/3-(m_p*math.cos(state[2])**2)/m_t))
        d = b-(m_p*l*c*math.cos(state[2]))/m_t

        state[0] = state[0] + tou*state[1]
        state[1] = state[1] + tou*d
        state[2] = state[2] + tou*state[3]
        state[3] = state[3] + tou*c

        G += R * gamma**g_pow
        g_pow += 1
        step += 1

    return G

def estimate_J(theta, N, M, stateFeature):
    G = []
    for i in range(N):
        G.append(runEpisode(theta, M, stateFeature))
    return sum(G)/N

def EvolutionSearch(nPerturbations, N, sigma, alpha, M, time_steps, stateFeature):
    n = M*4+1
    defineGuassian(n)
    theta = np.zeros(n)
    J_iter = []

    for t in range(time_steps):
        J = np.array([])
        weighted_epsilon = np.zeros((n,nPerturbations))
        for i in range(nPerturbations):
            epsilon = getPerturbation(n)
            J = np.append(J, estimate_J(theta + sigma*epsilon, N, M, stateFeature))
            weighted_epsilon[:,i] = J[-1]*epsilon

        theta += (alpha/(sigma*nPerturbations))*np.sum(weighted_epsilon,axis=1)
        #print(t, theta, estimate_J(theta, N, M))
        J_iter.append(estimate_J(theta, N, M, stateFeature))
    return J_iter

"""
def hyperSearch():

    #Default values of hyperparameters
    M = 1
    N = 1
    nPerturbations = 10
    sigma = 1e-1
    alpha = 1e-8

    #N_range = range(1,20,10)
    #M_range = range(1,10,5)
    #nPerturbations_range = range(20,42,20)
    #alpha_range = [round((10**(-i))**3,i*3) for i in range(5)]
    #sigma_range = range(20,82,20)

    trials = 5
    J_hyper = [[] for _ in range(trials)]
    J_hyper_sum = []

    #for sigma in sigma_range:
    for trial in range(trials):
        J_hyper[trial] = EvolutionSearch(nPerturbations, N, sigma/100, alpha, M)

    print(M, N, nPerturbations, alpha, sigma)
    J_hyper_sum.append(list(map(lambda x: x / trials, map(sum, zip(*J_hyper)))))

    J_std_dev = [0]*len(J_hyper_sum[0])

    for column in range(len(J_hyper[0])):
        for row in range(len(J_hyper)):
            J_std_dev[column] += (J_hyper[row][column]-J_hyper_sum[0][column])**2

    for i in range(len(J_std_dev)):
        J_std_dev[i] = math.sqrt(J_std_dev[i]/trials)

    # Display the plot
    plt.show()

    fig, ax = plt.subplots()
    #for j in range(len(J_hyper)/10):
    for i in range(len(J_hyper_sum)):
        ax.plot(range(time_steps),J_hyper_sum[i],label="J-"+str([M,N,nPerturbations,alpha,sigma]))

    ax.plot(range(time_steps), J_std_dev, label="Standard deviation")

    ax.legend()
    plt.xlabel("Policy update iterations")
    plt.ylabel("Return (J)/SD")
    plt.title("Mean and Standard Deviation Plot for "+str(time_steps)+" trials (M,N,nPer,al,si)")
    plt.legend(loc='upper right', bbox_to_anchor=(1, 0.8))
    plt.show()

hyperSearch()
"""










