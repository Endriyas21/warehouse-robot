import numpy as np
from utils import is_terminal_state, get_starting_location, get_next_action, get_next_location

def train_q_learning(q_values, rewards, epsilon, discount_factor, learning_rate, episodes=1000):
    for episode in range(episodes):
        row_index, column_index = get_starting_location(rewards)

        while not is_terminal_state(rewards, row_index, column_index):
            action_index = get_next_action(q_values, row_index, column_index, epsilon)
            old_row_index, old_column_index = row_index, column_index
            row_index, column_index = get_next_location(row_index, column_index, action_index)

            reward = rewards[row_index, column_index]
            old_q_value = q_values[old_row_index, old_column_index, action_index]
            temporal_difference = reward + (discount_factor * np.max(q_values[row_index, column_index])) - old_q_value

            new_q_value = old_q_value + (learning_rate * temporal_difference)
            q_values[old_row_index, old_column_index, action_index] = new_q_value

def get_shortest_path(q_values, start_row_index, start_column_index):
    if is_terminal_state(rewards, start_row_index, start_column_index):
        return []
    else:
        current_row_index, current_column_index = start_row_index, start_column_index
        shortest_path = []
        shortest_path.append([current_row_index, current_column_index])

        while not is_terminal_state(rewards, current_row_index, current_column_index):
            action_index = get_next_action(q_values, current_row_index, current_column_index, 1.)
            current_row_index, current_column_index = get_next_location(current_row_index, current_column_index, action_index)
            shortest_path.append([current_row_index, current_column_index])

        return shortest_path