HackerRank-city is an acyclic connected graph (or tree). Its not an ordinary place, the construction of the whole tree takes place in  steps. The process is described below:

It initially has  node.
At each step, you must create  duplicates of the current tree, and create  new nodes to connect all  copies in the following H shape:
nik2.png

At each  step, the tree becomes  times bigger plus  new nodes, as well as  new edges connecting everything together. The length of the new edges being added at step  is denoted by input .

Calculate the sum of distances between each pair of nodes; as these answers may run large, print your answer modulo .

Input Format

The first line contains an integer,  (the number of steps). The second line contains  space-separated integers describing , .

Constraints



Subtask
For  score 

Output Format

Print the sum of distances between each pair of nodes modulo .

Sample Input 0

1
1
Sample Output 0

29
Sample Input 1

2
2 1
Sample Output 1

2641
Explanation

Sample 0
In this example, our tree looks like this:

nik4.png

Let  denote the distance between nodes  and .

   .

We print the result of  as our answer.

Sample 1

In this example, our tree looks like this:nik city2.png

We calculate and sum the distances between nodes in the same manner as Sample 0 above, and print the result of our , which is .
