# Warehouse Robot Pathfinding with Q-Learning

This repository contains a project that demonstrates the use of Q-learning with temporal difference (TD) learning to train warehouse robots to find the shortest path between various locations in a warehouse. The robots are tasked with picking items from shelves and delivering them to a packaging area, ensuring maximum efficiency and productivity.

## Project Overview

In the context of e-commerce warehousing, "picking" refers to the task of gathering individual items from various locations within the warehouse to fulfill customer orders. After picking items from the shelves, the robots must bring the items to a specific location within the warehouse where they can be packaged for shipping.

## Key Features

- **Environment Setup**: The warehouse environment is represented as a grid with different states (locations), actions (movements), and rewards (incentives for reaching the goal).
- **Q-Learning Algorithm**: The project uses Q-learning with temporal difference (TD) learning to train the robots. The algorithm helps the robots learn the shortest path between the item packaging area and all other locations in the warehouse.
- **Helper Functions**: Various helper functions are provided to facilitate the training process, including functions to determine terminal states, choose random starting locations, and get the next action based on the epsilon-greedy policy.
- **Training and Evaluation**: The AI agent is trained over multiple episodes to learn the optimal paths, and the shortest paths are evaluated and displayed.

## Files and Structure

- `main.py`: Contains the main logic for setting up the environment, training the AI agent, and displaying the shortest paths.
- `environment.py`: Defines the environment, including states, actions, and rewards.
- `q_learning.py`: Contains the Q-learning algorithm and helper functions.
- `utils.py`: Contains utility functions such as checking terminal states and getting starting locations.

## How to Use

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/your-username/warehouse-robot.git
   cd warehouse-robot
   ```

2. **Run the Main Script**:

   ```sh
   python main.py
   ```

3. **Explore the Results**:
   - The script will display the shortest paths from various starting locations to the item packaging area.
   - You can modify the starting locations in the `main.py` file to test different scenarios.

## Dependencies

- Python 3.x
- NumPy

## Future Work

- Implement additional features such as obstacle avoidance and dynamic pathfinding.
- Extend the environment to include more complex warehouse layouts.
- Integrate with real-world robotic systems for practical applications.
