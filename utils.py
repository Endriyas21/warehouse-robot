import numpy as np

def is_terminal_state(rewards, current_row_index, current_column_index):
    if rewards[current_row_index, current_column_index] == -1.:
        return False
    else:
        return True

def get_starting_location(rewards):
    environment_rows, environment_columns = rewards.shape
    current_row_index = np.random.randint(environment_rows)
    current_column_index = np.random.randint(environment_columns)

    while is_terminal_state(rewards, current_row_index, current_column_index):
        current_row_index = np.random.randint(environment_rows)
        current_column_index = np.random.randint(environment_columns)

    return current_row_index, current_column_index

def get_next_action(q_values, current_row_index, current_column_index, epsilon):
    if np.random.random() < epsilon:
        return np.argmax(q_values[current_row_index, current_column_index])
    else:
        return np.random.randint(4)

def get_next_location(current_row_index, current_column_index, action_index):
    actions = ['up', 'right', 'down', 'left']
    new_row_index = current_row_index
    new_column_index = current_column_index

    if actions[action_index] == 'up' and current_row_index > 0:
        new_row_index -= 1
    elif actions[action_index] == 'right' and current_column_index < environment_columns - 1:
        new_column_index += 1
    elif actions[action_index] == 'down' and current_row_index < environment_rows - 1:
        new_row_index += 1
    elif actions[action_index] == 'left' and current_column_index > 0:
        new_column_index -= 1

    return new_row_index, new_column_index

def print_rewards(rewards):
    for row in rewards:
        print(row)