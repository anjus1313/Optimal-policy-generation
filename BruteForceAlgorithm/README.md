## Brute Force Method on Simple MDP

## Introduction:
The package consists of 2 files SimpleMDP.py and BruteForceOptimalPolicyGenerator.py.<br>

## Requirements:
This code has been tested with
- Python 3.11.5gi
<br>

Python libraries required
<br>
- numpy
- matplotlib

## Instructions to run the code:
  - Use the command 'python SimpleMDP.py' and 'python BruteForceOptimalPolicyGenerator.py' and to run the file.
  - Program to estimate J(π) by simulating many of the possible outcomes (returns)
    that might result from running π on the previously-defined MDP. Each simulation will produce a particular sequence of
    states, actions, and rewards, and, thus, a particular discounted return. Since J(π) is defined as the expected discounted
    return, you can construct an estimate of J(π), ˆJ(π), by averaging the discounted returns observed across N simulations

![Alt Text]("Images/SimpleMDP.png")