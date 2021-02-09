Roy has taken a liking to the Binary Search Trees(BST). He is interested in knowing the number of ways an array  of  integers can be arranged to form a BST. Thus, he tries a few combinations, and notes down the numbers at the odd levels and the numbers at the even levels.

You're given two values, alpha and beta. Can you calculate the sum of Liking of all possible BST's that can be formed from an array of  integers? Liking of each BST is defined as follows

(sum of numbers on even levels * alpha) - (sum of numbers on odd levels * beta)
Note

The root element is at level  ( Even )
The elements smaller or equal to the parent element are present in the left subtree, elements greater than or equal to the parent element are present in the right subtree. Explained here
If the answer is no less than , output the answer % .

(If the answer is less than , keep adding  until the value turns non negative.)

Input Format
The first line of input file contains an integer, , denoting the number of test cases to follow.
Each testcase comprises of  lines.
The first line contains , the number of integers.
The second line contains two space separated integers, alpha and beta.
The third line contains space separated  integers_, denoting the  integer in array .

Output Format
Output  lines. Each line contains the answer to its respective test case.

Constraints





Sample Input

4
1
1 1
1
2
1 1
1 2
3
1 1
1 2 3
5
1 1
1 2 3 4 5
Sample Output

1
0
6
54
Explanation

There are  test cases in total.

For the first test case, only  BST can be formed with 1 as the root node. Hence the Liking / sum is .

For the second test case, we get 2 BSTs of the form, the Liking of the first tree is  and , this sums to , hence the answer.

1                  2 
 \                /
  2              1
For the third test case, we get  BSTs. The Liking of each of the BST from left to right are  which sums to  and hence the answer.
1            2                 3          3      1
 \          / \               /          /        \
  2        1   3             1          2          3
   \                          \        /          /
    3                          2      1          2
Similarly, for the fourth test case, the answer is .
