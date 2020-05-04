We all know how to calculate  using  operations by multiplying  by  a total of  times. The drawback to this method is that  can be large, which makes exponentiation very slow.

There is a well known method called Russian Peasant Multiplication that you can read about here. Now let's use this to raise some complex numbers to powers!

You're given  queries where each query consists of four integers: , , , and . For each query, calculate  (where  is an imaginary unit) and then print the respective values of  and  as two space-separated integers on a new line.

Input Format

The first line contains a single integer, , denoting the number of queries.
Each of the  subsequent lines describes a query in the form of four space-separated integers: , , , and  (respectively).

Constraints

Output Format

For each query, print the two space-separated integers denoting the respective values of  and  on a new line.

Sample Input

3
2 0 9 1000
0 1 5 10
8 2 10 1000000000
Sample Output

512 0
0 1
880332800 927506432
Explanation

In the first query, we have , , , . We calculate the following:

