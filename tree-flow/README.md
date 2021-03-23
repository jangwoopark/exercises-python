Recall that a tree is an undirected, connected acyclic graph. We have a weighted tree, , with  vertices; let  be the total sum of edge weights on the path between nodes  and .

Let's consider all the matrices, , such that:

 for each  and 
We consider the total value of matrix  to be:

Calculate and print the maximum total value of  for a given tree, .

Input Format

The first line contains a single positive integer, , denoting the number of vertices in tree .
Each line  of the  subsequent lines contains three space-separated positive integers denoting the respective , , and  values defining an edge connecting nodes  and  (where ) with edge weight .

Constraints

Test cases with  have  of total score
Test cases with  have  of total score
Output Format

Print a single integer denoting the maximum total value of matrix  satisfying the properties specified in the Problem Statement above.

Sample Input

3
1 2 2
1 3 1
Sample Output

3
Explanation

In the sample case, matrix  is:

The sum of the elements of the first row is equal to .
