
Our unsung tower-breaking heroes (players  and ) only have one tower left, and they've decided to break it for a special game commemorating the end of  days of Game Theory! The rules are as follows:

 always moves first, and both players always move optimally.
Initially there is  tower of height .
The players move in alternating turns. The moves performed by each player are different:
At each turn,  divides the current tower into some number of smaller towers. If the turn starts with a tower of height  and  breaks it into  smaller towers, the following condition must apply: , where  denotes the height of the  new tower.
At each turn,  chooses some tower  of the  new towers made by  (where ). Then  must pay  coins to . After that,  gets another turn with tower  and the game continues.
The game is over when no valid move can be made by , meaning that .
's goal is to pay as few coins as possible, and 's goal is to earn as many coins as possible.
Can you predict the number of coins that  will earn?

Input Format

The first line contains a single integer, , denoting the number of test cases.
Each of the  subsequent lines contains a single integer, , defining the initial tower height for a test case.

Constraints

Output Format

For each test case, print a single integer denoting the number of coins earned by  on a new line.

Sample Input

3
4
2
7
Sample Output

6
4
8
Explanation

Test Case 0:
Our players make the following moves:

 splits the initial tower into  smaller towers of sizes  and .
 chooses the first tower and earns  coin.
 splits the tower into  smaller towers of sizes  and .
 chooses the first tower and earns  coin.
 splits the tower into  smaller towers of size .
 chooses the second tower and earns  coins.
The total number of coins earned by  is , so we print  on a new line.
