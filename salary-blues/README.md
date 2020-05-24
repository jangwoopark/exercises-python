Manager of HackerX company is having big trouble. Workers are very unhappy with the way salary is given to them. They want every worker to have the same salary, otherwise they will go on a strike.

Their current salaries are denoted by a sequence of N integers: A1, A2, A3 ... AN . Manager has decided to take action and make their salaries equal. He uses the following process until all salaries are equal. This method is called normalization:

a) Select any two different values from A.

b) Replace larger value with the difference of the two. Difference of two positive integers B and C is defined as |B-C|.

He knows that the final value will always be unique.
Now, Q queries are given. In each query you are given an integer K. K is the amount to be added to everyone's salary as bonus, before the normalization.

Input Format
First line contains, N and Q, the number of employees and the number of queries. Next line contains N space seperated positive integers denoting the array A. Next Q lines contain queries. Each query consists of one integer per line denoting K.

Output Format
For each query, print the normalized salary (which is same for everyone in the end) in one line.

Constraints
1 ≤ N ≤ 105
1 ≤ Q ≤ 105
1 ≤ A[i] ≤ 1014
0 ≤ K ≤ 109

Sample Input

4 2
9 12 3 6
0
3
Sample Output

3
3
Explanation
for sample input:
If 0 is added to every element of array A, it will remain same.
One way to normalise A is this:
1. Picking 12 and 3 gives: 9 9 3 6
2. Picking 3 and 6 gives: 9 9 3 3
3. Picking 9 and 3 gives: 6 9 3 3
4. Picking 9 and 3 gives: 6 6 3 3
5. Picking 6 and 3 gives: 3 6 3 3
6. Picking 6 and 3 gives: 3 3 3 3
