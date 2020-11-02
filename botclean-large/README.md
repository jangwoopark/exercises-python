MegaMaid is a robot whose function is to move through a matrix and clean all of its dirty cells. It's positioned in some cell of an  matrix of dirty (d) and clean (-) cells. It can perform five types of operations:

LEFT: Move one cell to the left.
RIGHT: Move one cell to the right.
UP: Move one cell up.
DOWN: Move one cell down.
CLEAN: Clean the cell.
Given the robot's current location and the configuration of dirty and clean cells in the matrix, print the next operation MegaMaid will perform (e.g., UP, CLEAN, etc.) on a new line.

Input Format

The first line contains two space-separated integers describing the respective  (row) and  (column) coordinates of MegaMaid's initial location.
The second line contains two space-separated integers describing the respective height, , and width, , of the matrix.
Each line  of the  subsequent lines contains a string of  characters describing row  in the matrix; each character  describes the character at location  according to the following key:

b denotes MegaMaid's location (in a clean cell).
d denotes a dirty cell.
- denotes a clean cell.
Note: If MegaMaid is initially located in a dirty cell, the cell will be marked with a d (not a b).

Constraints

Output Format

Print the next operation MegaMaid will perform (i.e., LEFT, RIGHT, UP, DOWN, CLEAN). It's important to only print the next operation, because your program will be called iteratively after performing each operation.

Sample Input

0 0
5 5
b---d
-d--d
--dd-
--d--
----d
Sample Output

RIGHT
Explanation

MegaMaid's next move would be to move RIGHT, resulting in the following next state:

-b--d
-d--d
--dd-
--d--
----d
