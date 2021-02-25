# Maze Game and Solver
This is a maze game, which can be played manually, or with an automatic solver.

## Manual Mode Instructions

### Running the game
Type the command:
python3 run.py {board_name}.txt

The list of boards can be found in the "boards" directory. You can create your own as well.

### Rules
#### Movement
WASDF to move left right up and down.
E to wait.

#### Fire and Water
Water space will give you a water bucket, which can be used to extinguish a flame. Stepping on fire without any water buckets will result in an instant loss.

#### Teleport
Teleport spaces are represented by numbers, which come in pairs. Landing on a teleport takes you to the opposite corresponding number.

