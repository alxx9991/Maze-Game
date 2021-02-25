# Maze Game and Solver
This is a maze game, which can be played manually, or with an automatic solver.

## Manual Mode Instructions

### Running the game
Type the command:  
python3 run.py {board_name}.txt

The list of boards can be found in the "boards" directory. You can create your own as well.

### Rules
#### Win Condition
Win by taking the monkey to the checkered flag.

#### Movement
WASDF to move left right up and down.
E to wait.

#### Fire and Water
Water space will give you a water bucket, which can be used to extinguish a flame. Stepping on fire without any water buckets will result in an instant loss.

#### Teleport
Teleport spaces are represented by numbers, which come in pairs. Landing on a teleport takes you to the opposite corresponding number. Pressing "E" on a teleport pad will take you back.

## Solver Mode Instructions
The solver can use either a DFS or BFS algorithm to solve the maze.  
Type the command:  
python3 solver.py {board_name}.txt {DFS/BFS}  
DFS will be less memory intensive, but may not always produce the shortest path.  
BFS will use more memory, especially for longer boards, however it always produces the shortest path.  
The solver has been slowed down on purpose to allow a visual representation of solving the maze. Comment out the "time.sleep()" line to increase solving speed.
