Given a long integer , count the number of values of  satisfying the following conditions:

where  and  are long integers and  is the bitwise XOR operator.

You are given  queries, and each query is in the form of a long integer denoting . For each query, print the total number of values of  satisfying the conditions above on a new line.

For example, you are given the value . Condition  requires that . The following tests are run:





We find that there are  values meeting the first condition:  and .

Function Description

Complete the theGreatXor function in the editor below. It should return an integer that represents the number of values satisfying the constraints.

theGreatXor has the following parameter(s):

x: an integer
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a long integer describing the value of  for a query.

Constraints

Subtasks

For  of the maximum score:

Output Format

For each query, print the number of values of  satisfying the given conditions on a new line.

Sample Input 0

2
2
10
Sample Output 0

1
5
Explanation 0

We perform the following  queries:

For  the only value of  satisfying  is . This also satisfies our other condition, as  and . Because we have one valid  and there are no more values to check, we print  on a new line.
For , the following values of  satisfy our conditions:






There are five valid values of .

Sample Input 1

2
5
100
Sample Output 1

2
27
Explanation 1

In the first case:


In the second case, the first 10 values are:











