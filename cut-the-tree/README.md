Anna loves graph theory! She has a tree where each vertex is numbered from  to , and each contains a data value.

The sum of a tree is the sum of all its nodes' data values. If she cuts an edge in her tree, she forms two smaller trees. The difference between two trees is the absolute value between their sums.

Given a tree, determine which edge to cut so that the resulting trees have a minimal difference between them, then return that difference.

For example, your tree's nodes have weights of . In this case, node numbers match their weights for convenience. In the diagram below, you have the following edges: .

image

The values are calculated as follows:

Edge    Tree 1  Tree 2  Absolute
Cut     Sum      Sum     Difference
1        8         13         5
2        9         12         3
3        6         15         9
4        4         17        13
5        5         16        11
The minimum absolute difference is .

Note: The tree is always rooted at vertex .

Function Description

Complete the cutTheTree function in the editor below. Return an integer that represents the minimal absolute difference achievable between the resultant two trees.

cutTheTree has the following parameter(s):

data: an array of integers that represent node values
edges: an 2 dimensional array of integer pairs where each pair represents an edge in the graph
Input Format

The first line contains an integer , the number of vertices in the tree.
The second line contains  space-separated integers, where each integer  denotes the value of .
Each of the  subsequent lines contains two space-separated integers  and  describing edge  in tree .

Constraints

, where .
Output Format

A single line containing the minimum difference possible for tree .

Sample Input

6
100 200 100 500 100 600
1 2
2 3
2 5
4 5
5 6
Sample Output

400
Explanation

We can visualize the initial, uncut tree as:

cut-the-tree.png

There are  edges we can cut:

Edge  results in 
Edge  results in 
Edge  results in 
Edge  results in 
Edge  results in 
The minimum difference is .
