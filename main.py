import numpy as np
from environment import environment_rows, environment_columns, rewards, actions
from q_learning import train_q_learning, get_shortest_path
from utils import print_rewards

# Define training parameters
epsilon = 0.9  # the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9  # discount factor for future rewards
learning_rate = 0.9  # the rate at which the AI agent should learn

# Initialize Q-values
q_values = np.zeros((environment_rows, environment_columns, len(actions)))

# Train the AI agent using Q-learning
train_q_learning(q_values, rewards, epsilon, discount_factor, learning_rate)

print('Training complete!')

# Display a few shortest paths
print(get_shortest_path(q_values, 3, 9))  # starting at row 3, column 9
print(get_shortest_path(q_values, 5, 0))  # starting at row 5, column 0
print(get_shortest_path(q_values, 9, 5))  # starting at row 9, column 5

# Display an example of reversed shortest path
path = get_shortest_path(q_values, 5, 2)  # go to row 5, column 2
path.reverse()
print(path)