You are given  unweighted, undirected graphs, , , and , with  vertices each, where the  graph has  edges and the vertices in each graph are numbered from  through . Find the number of ordered triples , where , , such that there is an edge  in , an edge  in , and an edge  in .

Input Format

The first line contains single integer, , denoting the number of vertices in the graphs. The subsequent lines define , , and . Each graph is defined as follows:

The first line contains an integer, , describing the number of edges in the graph being defined.
Each line  of the  subsequent lines (where ) contains  space-separated integers describing the respective nodes,  and  connected by edge .
Constraints

, and 
Each graph contains no cycles and any pair of directly connected nodes is connected by a maximum of  edge.
Output Format

Print a single integer denoting the number of distinct  triples as described in the Problem Statement above.

Sample Input

3
2
1 2
2 3
3
1 2
1 3
2 3
2
1 3
2 3
Sample Output

3
Explanation

There are three possible triples in our Sample Input:

Thus, we print  as our output.
