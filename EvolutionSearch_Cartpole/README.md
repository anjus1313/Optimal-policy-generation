## Evolution Strategies Algorithm in Cartpole domain

## Introduction:
The package consists of 3 files FindRange_v_w_dot.py, ESSearch.py and HyperparameterSearch.py.<br>
- FindRange_v_w_dot.py: Contains the code to find then range of velocity and angular velocity.
- ESSearch.py: Contains the Evolution strategies implementation.
- HyperparameterSearch.py: Contains the code to run Evolution Strategies on default hyperparameters or to perform hyperparameter tuning.
## Requirements:
This code has been tested with
- Python 3.11.5gi
<br>

Python libraries required
<br>
- numpy
- matplotlib
- random
- math

## Instructions to run the code:
#### Finding the range of Velocity and Angular velocity of cartpole:
- Use the command 'python FindRange_v_w_dot.py' to run the file.
- The system output provides the minimum and maximum of each of those variables.

#### Running Evolution Strategies algorithm for specific hyperparameters:
- Pre-run setup
  - Open the HyperparameterSearch.py file in notepad or other preferred text editor.
  - Set number of iterations in 'time_steps' (Line-5)
  - Set number of trials/runs in 'trials' (Line-6)
  - Set the values for hyperparameters in the variables in Lines 9-13.
  - Set state feature representation in the variable stateFeature with "Cos" or "Sine".
- Run Evolution Strategies
  - Use the command 'python HyperparameterSearch.py' to run the file.
  - The output plot provides the mean and standard deviation of returns over a number of trials.

#### Running Evolution Strategies algorithm for tuning hyperparameters:
- Pre-run setup
  - Comment the hyperparameter to be tuned (eg. alpha) (Line-9-13).
  - Uncomment the same hyperparameter in Lines-18-22 and specify the range.
  - Uncomment Line-27 and change variable name to the 'hyperparameter' and 'hyperparameter'_range to be tuned.
  - Add 1-tab indent for Lines-28,29,31,32. 
- Run Evolution Strategies
  - Use the command 'python HyperparameterSearch.py' to run the file.
  - The output plot provides the mean of returns over a number of trials for different values of the hyperparameter to be tuned.


