After their success in coming up with Fun Game, Kyle and Mike invented another game having the following rules:

The game starts with an -element sequence, , and is played by two players,  and .
The players move in alternating turns, with  always moving first. During each move, the current player chooses one of the asterisks () in the above sequence and changes it to either a + (plus) or a - (minus) sign.
The game ends when there are no more asterisks () in the expression. If the evaluated value of the sequence is divisible by , then  wins; otherwise,  wins.
Given the value of , can you determine the outcome of the game? Print  if  will win, or  if  will win. Assume both players always move optimally.

Input Format

The first line of input contains a single integer , denoting the number of test cases. Each line  of the  subsequent lines contains an integer, , denoting the maximum exponent in the game's initial sequence.

Constraints

Output Format

For each test case, print either of the following predicted outcomes of the game on a new line:

Print  if  will win.
Print  if  will win.
Sample Input

1
2  
Sample Output

First
Explanation

In this case, it doesn't matter in which order the asterisks are chosen and altered. There are  different courses of action and, in each one, the final value is not divisible by  (so  always loses and we print  on a new line).

Possible options:

