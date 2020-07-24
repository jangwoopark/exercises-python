You and your friend decide to play a game using a stack consisting of N bricks. In this game, you can alternatively remove 1, 2 or 3 bricks from the top, and the numbers etched on the removed bricks are added to your score. You have to play so that you obtain the maximum possible score. It is given that your friend will also play optimally and you make the first move.

As an example, bricks are numbered . You can remove either ,  or . For your friend, your moves would leave the options of  to  elements from  leaving  for you (total score = ),  or . In this case, it will never be optimal for your friend to take fewer than the maximum available number of elements. Your maximum possible score is , achievable two ways:  first move and  the second, or  in your first move.

Function Description

Complete the bricksGame function in the editor below. It should return an integer that represents your maximum possible score.

bricksGame has the following parameter(s):

arr: an array of integers
Input Format

The first line will contain an integer , the number of test cases.

Each of the next  pairs of lines are in the following format:
The first line contains an integer , the number of bricks in .
The next line contains  space-separated integers $arr[i].

Constraints




Output Format

For each test case, print a single line containing your maximum score.

Sample Input

2
5
999 1 1 1 0
5
0 1 1 1 999
Sample Output

1001
999
Explanation

In first test case, you will pick 999,1,1. If you play in any other way, you will not get a score of 1001.
In second case, best option will be to pick up the first brick (with 0 score) at first. Then your friend will choose the next three blocks, and you will get the last brick.
