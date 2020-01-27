Sherlock is given an array of  integers (,  ...  by Watson. Now Watson asks Sherlock how many different pairs of indices  and  exist such that  is not equal to  but  is equal to .

That is, Sherlock has to count the total number of pairs of indices  where   AND .

Input Format
The first line contains , the number of test cases.  test cases follow.
Each test case consists of two lines; the first line contains an integer , the size of array, while the next line contains  space separated integers.

Output Format
For each test case, print the required answer on a different line.

Constraints



Sample input

2
3
1 2 3
3
1 1 2
Sample output

0
2
Explanation
In the first test case, no two pair of indices exist which satisfy the given condition.
In the second test case as A[0] = A[1] = 1, the pairs of indices (0,1) and (1,0) satisfy the given condition.
