You have a pile of  stones that you want to split into multiple piles, as well as a set, , of  distinct integers. We define a move as follows:

First, choose a pile of stones. Let's say that the chosen pile contains  stones.
Next, look for some  such that  and  is divisible by  (i.e.,  is a factor of ); if such an  exists, you can split the pile into  equal smaller piles.
You are given  queries where each query consists of  and . For each query, calculate the maximum possible number of moves you can perform and print it on a new line.

Input Format

The first line contains an integer, , denoting the number of queries. The  subsequent lines describe each query in the following format:

The first line contains two space-separated integers describing the respective values of  (the size of the initial pile in the query) and  (the size of the set in the query).
The second line contains  distinct space-separated integers describing the values in set .
Constraints

Subtask

 for  of the maximum score.
Output Format

For each query, calculate the maximum possible number of moves you can perform and print it on a new line.

Sample Input 0

1
12 3
2 3 4
Sample Output 0

4
Explanation 0

Initially there is a pile with  stones:

image

You can make a maximal  moves, described below:

Select  from  and split it into  equal piles of size  to get:
image
Select  from  and split a pile of size  into  equal piles of size  to get:
image

Repeat the previous move again on another pile of size  to get:
image

Repeat the move again on the last pile of size  to get:
image
As there are no more available moves, we print  (the number of moves) on a new line.
