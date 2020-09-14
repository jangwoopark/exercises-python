You are standing at point  on an infinite plane. In one step, you can move from some point  to any point  as long as the Euclidean distance, , between the two points is either  or . In other words, each step you take must be exactly  or  in length.

You are given  queries in the form of , , and . For each query, print the minimum number of steps it takes to get from point  to point  on a new line.

Input Format

The first line contains an integer, , denoting the number of queries you must process.
Each of the  subsequent lines contains three space-separated integers describing the respective values of , , and  for a query.

Constraints

Output Format

For each query, print the minimum number of steps necessary to get to point  on a new line.

Sample Input 0

3
2 3 1
1 2 0
3 4 11
Sample Output 0

2
0
3
Explanation 0

We perform the following  queries:

One optimal possible path requires two steps of length : . Thus, we print the number of steps, , on a new line.
The starting and destination points are both , so we needn't take any steps. Thus, we print  on a new line.
One optimal possible path requires two steps of length  and one step of length : . Thus, we print  on a new line.
