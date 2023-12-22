from ESSearch import EvolutionSearch
import math
import matplotlib.pyplot as plt

time_steps = 50
trials = 5

#Default values of hyperparameters
M = 1
N = 1
nPerturbations = 50
sigma = 0.01
alpha = 1e-6
stateFeature = "Cos"    #Cos/Sine

#For tuning

#N_range = range(1,20,10)
#M_range = range(1,10,5)
#nPerturbations_range = range(20,42,20)
#alpha_range = [round((10**(-i))**3,i*3) for i in range(5)]
#sigma_range = range(20,22,20)

J_hyper = [[] for _ in range(trials)]
J_hyper_sum = []

#for M in M_range:
for trial in range(trials):
    J_hyper[trial] = EvolutionSearch(nPerturbations, N, sigma, alpha, M, time_steps,stateFeature)

print(M, N, nPerturbations, alpha, sigma)
J_hyper_sum.append(list(map(lambda x: x / trials, map(sum, zip(*J_hyper)))))

J_std_dev = [0]*len(J_hyper_sum[0])

for column in range(len(J_hyper[0])):
    for row in range(len(J_hyper)):
        J_std_dev[column] += (J_hyper[row][column]-J_hyper_sum[0][column])**2

for i in range(len(J_std_dev)):
    J_std_dev[i] = math.sqrt(J_std_dev[i]/trials)

fig, ax = plt.subplots()

for i in range(len(J_hyper_sum)):
    ax.plot(range(time_steps),J_hyper_sum[i],label="J-"+str([M,N,nPerturbations,alpha,sigma]))

ax.plot(range(time_steps), J_std_dev, label="Standard deviation")

ax.legend()
plt.xlabel("Policy update iterations")
plt.ylabel("Return (J)/SD")
plt.title("Mean and Standard Deviation Plot for "+str(trials)+" trials (M,N,nPer,al,si)")
plt.legend(loc='upper right', bbox_to_anchor=(1, 0.8))
plt.show()

