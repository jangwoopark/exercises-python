N Puzzle is a sliding blocks game that takes place on a k * k grid with ((k * k) - 1) tiles each numbered from 1 to N. Your task is to reposition the tiles to their proper order.

Input Format

The first line of the input contains an integer k, the size of the square grid. k * k lines follow each line containing an integer I on the tile starting from the top left to bottom right. The empty cell is represented by the number 0.

N = (k * k) -1
0 <= I <= N

Constraints

3 <= k <= 5

Output Format

The first line contains an integer, M, the number of moves your algorithm has taken to solve the N-Puzzle. M lines follow. Each line indicating the movement of the empty cell (0).

A grid is considered solved if it is of the following configuration.

0 1 2
3 4 5
6 7 8
Sample Input

3
0
3
8
4
1
7
2
6
5
Sample Output

70
RIGHT
DOWN
...
...
...
Explanation

The board given as input is

0 3 8
4 1 7
2 6 5
After RIGHT, the board's configuration is

3 0 8
4 1 7
2 6 5
Task

Print all the moves made from the given configuration to the final solved board configuration.

Scoring

On successfully solving the puzzle, your score will be k * k.
