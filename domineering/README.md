Domineering is a mathematical game played between two players who alternate by placing a domino of size 2x1 on an square board. The first player places the dominoes vertically and the second player places the dominoes horizontally on the board. The player unable to place his domino on the board loses.

Input Format

The game takes place on an 8x8 board. The first player is represented by v (ascii value: 118) and the second player by h (ascii value: 104). Empty cell is denoted by - (ascii value: 45) and a domino occupied cell is denoted by either v or h. The top left of the board is (0,0) and the bottom right is (7,7)

The first line denotes the character of the player who is playing. The next 8 lines contains 8 characters each representing the board.

Sample Input

v
-v------
-vhh----
---v----
---v----
---hh---
--------
--------
--------
Sample Output

2 1
For the first player, a move is denoted by its upper square. Here, the first player to place the domino at (2,1) and (3,1) outputs the position as (2,1) which is its upper square.

Sample Input

h
-v------
-vhh----
-v-v----
-v-v----
---hh---
--------
--------
--------
Sample Output

4 1
For the second player, a move is denoted by its left square. Here, the second player to place the domino at (4,1) and (4,2) outputs the position as (4,1) which is its left square.

Complete the function nextMove that takes a char player and an 8x8 board as input to print the next move. Your output must be two integers with a single space separating them.
