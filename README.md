# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: In general, our Sudoku solver contains two different steps:
     - reduction step, where we extract as more information from the curent sudoku
       configuration as we can;
     - search step, where we make some assumption to be able to proceed. 
       We use this step only if we cannot solve sudoku directly, without assumptions.
       
   Search step can be time-consuming as it, in fact, requires us to solve 
   several variations of the initial sudoku to check which one is a solution.
   Thus, it is important to have as less search steps as we can by improving 
   reduction step quality. 
   
   So, the more reduction strategies we have the better. 
   
   Naked Twins strategy itself is based on the simple fact: if, in some unit, 
   we have 2 boxes with same 2 (and only 2) possible values, then those 2 values 
   are impossible for all other boxes in this unit. 
   In my naked_twins implementation, for each unit I do: 
      - find a value(s) of length 2 that appears in the unit exactly twice 
      - exclude both digits of that value from all other boxes in unit
   


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Diagonal sudoku does not introduce additional chalange as compared to 
   normal sudoku. I would say it even makes it easier to solve: more constraints
   means more information and more reductions at each step.
   From the implementation point of view diagonal sudoku is also simple. 
   As we already have a framework that propagates constraints across all units,
   diagonal sudoku is just a matter of additing two additional units into 
   unitlist: one unit per diagonal.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.