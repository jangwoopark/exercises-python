Consider an -integer sequence, . We perform a query on  by using an integer, , to calculate the result of the following expression:

In other words, if we let , then you need to calculate .

Given  and  queries (each query consists of an integer, ), print the result of each query on a new line.

Input Format

The first line consists of two space-separated integers describing the respective values of  and .
The second line consists of  space-separated integers describing the respective values of .
Each of the  subsequent lines contains a single integer denoting the value of  for that query.

Constraints

Output Format

For each query, print an integer denoting the query's answer on a new line. After completing all the queries, you should have printed  lines.

Sample Input 0

5 5
33 11 44 11 55
1
2
3
4
5
Sample Output 0

11
33
44
44
55
Explanation 0

For , the answer is

.
For , the answer is
.
For , the answer is
.
For , the answer is
.
For , the answer is
.
Sample Input 1

5 5
1 2 3 4 5
1
2
3
4
5
Sample Output 1

1
2
3
4
5
Explanation 1

For each query, the "prefix" has the least maximum value among the consecutive subsequences of the same size.
