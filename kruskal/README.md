Given an undirected weighted connected graph, find the Really Special SubTree in it. The Really Special SubTree is defined as a subgraph consisting of all the nodes in the graph and:

There is only one exclusive path from a node to every other node.
The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.
No cycles are formed
To create the Really Special SubTree, always pick the edge with smallest weight. Determine if including it will create a cycle. If so, ignore the edge. If there are edges of equal weight available:

Choose the edge that minimizes the sum  where  and  are vertices and  is the edge weight.
If there is still a collision, choose any of them.
Print the overall weight of the tree formed using the rules.

For example, given the following edges:

u	v	wt
1	2	2
2	3	3
3	1	5
First choose  at weight . Next choose  at weight . All nodes are connected without cycles for a total weight of .

Function Description

Complete the  function in the editor below. It should return an integer that represents the total weight of the subtree formed.

kruskals has the following parameters:

g_nodes: an integer that represents the number of nodes in the tree
g_from: an array of integers that represent beginning edge node numbers
g_to: an array of integers that represent ending edge node numbers
g_weight: an array of integers that represent the weights of each edge
Input Format

The first line has two space-separated integers  and , the number of nodes and edges in the graph.

The next  lines each consist of three space-separated integers ,  and , where  and  denote the two nodes between which the undirected edge exists and  denotes the weight of that edge.

Constraints

**Note: ** If there are edges between the same pair of nodes with different weights, they are to be considered as is, like multiple edges.

Output Format

Print a single integer denoting the total weight of the Really Special SubTree.

Sample Input 1

CopyDownload
Undirected Weighed Graph: g
1
2
5
3
3
4
7
4
5
6

 
4 6
1 2 5
1 3 3
4 1 6
2 4 7
3 2 4
3 4 5
Sample Output 1

12
Explanation 1

The graph given in the test case is shown above.

Applying Kruskal's algorithm, all of the edges are sorted in ascending order of weight.

After sorting, the edge choices are available as :

 and 

Select 2 \rightarrow 3 (w=4)$ because it has the lowest weight without creating a cycle

The edge  would form a cycle, so it is ignored

Select  to finish the MST yielding a total weight of 

image


Sample Input 2

CopyDownload
Undirected Weighed Graph: g
1
2
20
3
50
4
70
5
90
30
40
60

 
5 7
1 2 20
1 3 50
1 4 70
1 5 90
2 3 30
3 4 40
4 5 60
Sample Output 2

150
Explanation 2

Given the graph above, select edges  with weights .
