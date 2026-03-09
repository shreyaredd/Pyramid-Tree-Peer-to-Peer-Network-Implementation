# Binary Tree Search Simulation

This project implements a network of 15 nodes structured as a complete binary tree. The goal is to demonstrate how a Depth First Search (DFS) algorithm traverses a hierarchical network to locate a specific resource.

### Network Structure
The nodes are organized in a standard binary tree where each parent node connects to two children.
* Node 0 acts as the root.
* For any node *i*, the children are located at *2i + 1* and *2i + 2*.



### Search Algorithm (DFS)
The search uses a recursive Depth First Search approach. Instead of checking every node at a single level, the algorithm "dives" as deep as possible down one branch before backtracking to the nearest unexplored junction. 

This method is useful for discovering resources in nested data structures or hierarchical file systems.



### Execution
To run the simulation:
1. Open a terminal in the project folder.
2. Run `python main.py`.
3. Provide a starting node (0-14) and the target resource ID when prompted.
