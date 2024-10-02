import numpy as np

# Define the shape of the environment (i.e., its states)
environment_rows = 11
environment_columns = 11

# Create a 2D numpy array to hold the rewards for each state
rewards = np.full((environment_rows, environment_columns), -100.)
rewards[0, 5] = 100.  # set the reward for the packaging area (i.e., the goal) to 100

# Define aisle locations (i.e., white squares) for rows 1 through 9
aisles = {}  # store locations in a dictionary
aisles[1] = [i for i in range(1, 10)]
aisles[2] = [1, 7, 9]
aisles[3] = [i for i in range(1, 8)]
aisles[3].append(9)
aisles[4] = [3, 7]
aisles[5] = [i for i in range(11)]
aisles[6] = [5]
aisles[7] = [i for i in range(1, 10)]
aisles[8] = [3, 7]
aisles[9] = [i for i in range(11)]

# Set the rewards for all aisle locations (i.e., white squares)
for row_index in range(1, 10):
    for column_index in aisles[row_index]:
        rewards[row_index, column_index] = -1.

# Define actions
# numeric action codes: 0 = up, 1 = right, 2 = down, 3 = left
actions = ['up', 'right', 'down', 'left']