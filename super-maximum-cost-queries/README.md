Victoria has a tree, , consisting of  nodes numbered from  to . Each edge from node  to  in tree  has an integer weight, .

Let's define the cost, , of a path from some node  to some other node  as the maximum weight () for any edge in the unique path from node  to node .

Victoria wants your help processing  queries on tree , where each query contains  integers,  and , such that . For each query, she wants to print the number of different paths in  that have a cost, , in the inclusive range .

It should be noted that path from some node  to some other node  is considered same as path from node  to  i.e  is same as .

Input Format

The first line contains  space-separated integers,  (the number of nodes) and  (the number of queries), respectively.
Each of the  subsequent lines contain  space-separated integers, , , and , respectively, describing a bidirectional road between nodes  and  which has weight .
The  subsequent lines each contain  space-separated integers denoting  and .

Constraints

Scoring

 for  of the test data.
 for  of the test data.
Output Format

For each of the  queries, print the number of paths in  having cost  in the inclusive range  on a new line.

Sample Input

5 5
1 2 3
1 4 2
2 5 6
3 4 1
1 1
1 2
2 3
2 5
1 6
Sample Output

1
3
5
5
10
Explanation

: 
: 
: 
: 
...etc.
