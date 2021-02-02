You are given a list of  numbers . For each element at position  (), we define  and  as:
 = closest index j such that j < i and . If no such j exists then  = 0.
 = closest index k such that k > i and . If no such k exists then  = 0.

We define  =  * . You need to find out the maximum  among all i.

Input Format

The first line contains an integer , the number of integers. The next line contains the  integers describing the list a[1..N].

Constraints



Output Format

Output the maximum  among all indices from  to .

Sample Input

5
5 4 3 4 5
Sample Output

8
Explanation

We can compute the following:






The largest of these is 8, so it is the answer.
