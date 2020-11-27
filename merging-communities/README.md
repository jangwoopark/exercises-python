People connect with each other in a social network. A connection between Person  and Person  is represented as . When two persons belonging to different communities connect, the net effect is the merger of both communities which  and  belongs to.

At the beginning, there are  people representing  communities. Suppose person  and  connected and later  and  connected, then ,, and  will belong to the same community.

There are two type of queries:

 communities containing person  and  merged (if they belong to different communities).

 print the size of the community to which person  belongs.

Input Format

The first line of input will contain integers  and , i.e. the number of people and the number of queries.
The next  lines will contain the queries.

Constraints :



Output Format

The output of the queries.

Sample Input

3 6
Q 1
M 1 2
Q 2
M 2 3
Q 3
Q 2
Sample Output

1
2
3
3
Explanation

Initial size of each of the community is .
