## TD-learning, SARSA and Q-learning implementation

## Introduction:
The package consists of 5 files TD_learning.py, SARSA_2_a_b.py, SARSA_2_c.py, Q_learning_3_a_b.py, Q_learning_3_c.py<br>
- TD_learning.py: It implements the TD learning algorithm to learn the near-optimal value function.
- SARSA_2_a_b.py: It implements the SARSA learning algorithm to learn the near-optimal policy. 
- SARSA_2_c.py: It implements the SARSA learning algorithm to learn the near-optimal policy.
- Q_learning_3_a_b.py: It implements the Q-learning algorithm to learn the near-optimal policy.
- Q_learning_3_c.py: It implements the Q-learning algorithm to learn the near-optimal policy.
## Requirements:
This code has been tested with
- Python 3.11.5
  <br>

Python libraries required
<br>
- numpy
- matplotlib
- math

## Instructions to run the code:
#### Running the TD learning algorithm:
- Use the command 'python TD_learning.py' to run the file.
- The system output displays the Average Value function, max norm between the learned value function and optimal value function.
- It also displays the average number of episodes and the standard deviation.
#### Running the SARSA learning algorithm:
- Use the command 'python SARSA_2_a_b.py' to run the file.
- This generates the Episodes vs steps and Average MSE learning curve plots.
##### Question 2c:
- Use the command 'python SARSA_2_c.py' to run the file.
- The system output displays the greedy policy learned along with the value function.
#### Running the Q-learning algorithm:
##### Question 3a, 3b:
- Use the command 'python Q_learning_3_a_b.py' to run the file.
- This generates the Episodes vs steps and Average MSE learning curve plots.
##### Question 3c:
- Use the command 'python Q_learning_3_c.py' to run the file.
- The system output displays the greedy policy learned along with the value function.


