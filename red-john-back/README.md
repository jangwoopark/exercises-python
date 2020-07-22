Red John has committed another murder. This time, he doesn't leave a red smiley behind. Instead he leaves a puzzle for Patrick Jane to solve. He also texts Teresa Lisbon that if Patrick is successful, he will turn himself in. The puzzle begins as follows.

There is a wall of size 4xn in the victim's house. The victim has an infinite supply of bricks of size 4x1 and 1x4 in her house. There is a hidden safe which can only be opened by a particular configuration of bricks. First we must calculate the total number of ways in which the bricks can be arranged so that the entire wall is covered. The following diagram shows how bricks might be arranged to cover walls where :

image

There is one more step to the puzzle. Call the number of possible arrangements . Patrick must calculate the number of prime numbers  in the inclusive range .

As an example, assume . From the diagram above, we determine that there is only one configuration that will cover the wall properly.  is not a prime number, so .

A more complex example is . The bricks can be oriented in  total configurations that cover the wall. The two primes  and  are less than or equal to , so .

image

Function Description

Complete the redJohn function in the editor below. It should return the number of primes determined, as an integer.

redJohn has the following parameter(s):

n: an integer that denotes the length of the wall
Input Format

The first line contains the integer , the number of test cases.
Each of the next  lines contains an integer , the length of the  wall.

Constraints

Output Format

Print the integer  on a separate line for each test case.

Sample Input

2
1
7
Sample Output

0
3
Explanation

For , the brick can be laid in 1 format only: vertically.


The number of primes  is .

For , one of the ways in which we can lay the bricks is

Red John

There are  ways of arranging the bricks for  and there are  primes .
