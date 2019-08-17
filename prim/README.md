Given a graph which consists of several edges connecting its nodes, find a subgraph of the given graph with the following properties:

The subgraph contains all the nodes present in the original graph.
The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.
It is also required that there is exactly one, exclusive path between any two nodes of the subgraph.
One specific node  is fixed as the starting point of finding the subgraph using Prim's Algorithm. 
Find the total weight or the sum of all edges in the subgraph.

image
For example, consider a graph with  nodes. Possible edges are  weight ,  weight  and  weight . Starting from node , we select the lower weight path, i.e. , weight . From node , there is only one path left,  weight . We have all nodes connected at a cost of .

Function Description

Complete the prims function in the editor below. It should return and integer that represents the minimum weight to connect all nodes in the graph provided.

prims has the following parameter(s):

n: an integer that represents the number of nodes in the graph
edges: a two-dimensional array where each element contains three integers, two nodes numbers that are connected and the weight of that edge
start: an integer that represents the number of the starting node
Input Format

The first line has two space-separated integers  and , the number of nodes and edges in the graph.

Each of the next  lines contains three space-separated integers ,  and , the end nodes of , and the edge's weight. 
The last line has an integer , denoting the starting node.

Constraints

 
 
 
 
There may be multiple edges between two nodes.

Output Format

Print a single integer denoting the total weight of the subgraph.

Sample Input 0

5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1
Sample Output 0

15
Explanation 0

The graph given in the test case is shown as :

image

The starting node is  (in the given test case)
Applying the Prim's algorithm, edge choices available at first are :

 (WT. 3) and  (WT. 4) , out of which  is chosen (smaller weight of edge).

Now the available choices are :

 (WT. 4) ,  (WT. 5) ,  (WT. 2) and  (WT. 6) , out of which  is chosen by the algorithm.

Following the same method of the algorithm, the next chosen edges , sequentially are :

 and .

Hence the overall sequence of edges picked up by Prim's are:


and the total weight of the MST (minimum spanning tree) is : 
