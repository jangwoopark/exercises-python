This problem introduces you to Markov Models and Simulation.

Markov is travelling in a train and he is bored. He takes out his Snakes and Ladders game and decides to play it all by himself. The die he plays with, is biased. Given the configuration of the Snakes and Ladders board, and the different probabilities with which the 6 different space of the die might appear; your task is to count the expected number of die rolls in which Markov will manage to move his peg from Square 1 to Square 100.

A few notes about the Snakes and Ladders game

Those who are not familiar with this game might get a decent idea from this Wikipedia page: Snakes And Ladders

Assume that you will always deal with a 10x10 board as described on the page above. There will be not more than fifteen snakes and fifteen ladders.

You will be given the different probabilities with which the different faces of the biased die might show up.

When a player reaches a square which is the base of a ladder, he has to climb up the ladder- (s)he has no choice. The ladder always leads to a "higher" square, which is closer to the top (100).

When a player reaches a square which has the mouth of a snake, (s)he will always end up at the square which corresponds to to tail of the snake- (s)he goes down and has no choice.

A die roll which would cause the player to land up at a square greater than 100, goes wasted, and the player remains at his original square. Such as a case when the player is at Square Number 99, rolls the die, and ends up with 5.

Simulate rolls of the die as per the given probabilities. For each board configuration, simulate 5000 games, and record the number of die rolls required to reach Square Number 100, after starting from Square Number 1. Take the average of these numbers for these 5000 games; this gives us a fair idea of the expected number of die rolls required to complete the game for a given board configuration.

The results of simulations are approximations and they vary a little bit, so we will allow a deviation of +/- 10% from the expected answers which we arrived at by averaging over a number of simulations. Your score for a given test file will be proportional to the number of tests which you manage to pass.

Rounds in which the game hasn't terminated (i.e. square #100 hasn't been reached) after even 1000 rolls of the die can be terminated and ignored.

Input Format
First line contains the number of tests, T. This is followed by 4T lines. There are 4 lines per test configuration and in each test: The first line is a list of six comma-separated probabilities with which different faces of the die appear.
The second line contains the number of ladders and snakes, separated by a comma.
The third is a list of comma separated pairs indicating the starting and ending squares of the ladders.
The fourth is a list of comma separated pairs indicating the starting and ending (mouth and tail) squares of the snakes.

Output Format For each of the T test cases, output one integer, each on a new line, which is the expected number of rolls of the die, which you have obtained either via computation or via simulation.

Sample Input

3
0.32,0.32,0.12,0.04,0.07,0.13
3,7
32,62 42,68 12,98
95,13 97,25 93,37 79,27 75,19 49,47 67,17
0.39,0.05,0.14,0.05,0.12,0.25
5,8
32,62 44,66 22,58 34,60 2,90
85,7 63,31 87,13 75,11 89,33 57,5 71,15 55,25
0.54,0.02,0.02,0.01,0.3,0.11
4,9
8,52 6,80 26,42 2,72
51,19 39,11 37,29 81,3 59,5 79,23 53,7 43,33 77,21
Explanation of the Input

line1: The first line contains '3': This is the number of board configurations provided, i.e. there are 3 tests.

line 2: This contains the comma separated probabilities of the different faces of the die showing up. Face 1 shows up with probability 0.32, face 2 shows up with probability 0.32, face 3 shows up with probability 0.12 and so on.

line 3: Number of ladders and snakes, separated by commas. There are 3 ladders and 7 snakes.

line 4: Pairs of starting and ending squares of ladders. The first ladder starts at square 32 and takes the player all the way to square 62. The second ladder starts at square 42 and takes the player all the way to square 68. There are commas between the starting and ending square of each ladder; and there are spaces between each such pair.

line 5: Pairs of starting and ending squares of snakes. The first snake starts at square 95 and takes the player down to square 13. The second snake starts at square 97 and takes the player all the way down to square 25. There are commas between the starting and ending square of each snake; and there are spaces between each such pair.

And so on, for the other 2 board configurations.

Sample Output
Please note that as this is a simulation challenge it is not necessary that your answers should match these values exactly.

160
95
162
Explanation

Since this is a problem involving simulation, a reasonable margin of deviation from these numbers will be tolerated, as explained in the scoring section. For the first test, the expected number of die rolls to reach the destination square (100) is 160.
For the second test, it is 95 die rolls.
For the third test, it is 162 die rolls.

Scoring

If there are N tests in a particular test case file, your score will be:

(maxScore for test case file) * C/N

Where C is the number of correct answers in your output; which are within +/- 10% of the expected values which we arrived at by averaging over a number of simulations.
