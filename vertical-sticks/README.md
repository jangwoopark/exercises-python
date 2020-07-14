Given an array of integers , we have  line segments, such that, the endpoints of  segment are  and . Imagine that from the top of each segment a horizontal ray is shot to the left, and this ray stops when it touches another segment or it hits the y-axis. We construct an array of  integers, , where  is equal to length of ray shot from the top of segment . We define .

For example, if we have , then , as shown in the picture below:

vertical.png

For each permutation  of , we can calculate . If we choose a uniformly random permutation  of , what is the expected value of ?

Input Format

The first line contains a single integer T (1 <=T<= 100). T test cases follow.
The first line of each test-case is a single integer N (1 <= n <= 50), and the next line contains positive integer numbers  separated by a single space ().

Output Format

For each test-case output expected value of , rounded to two digits after the decimal point.

Sample Input

6
3
1 2 3
3
3 3 3
3
2 2 3
4
10 2 4 4
5
10 10 10 5 10
6
1 2 3 4 5 6
Sample Output

4.33
3.00
4.00
6.00
5.80
11.15
Explanation

Case 1: We have ,
.
Average of these values is 4.33.
Case 2: No matter what the permutation is, , so the answer is 3.00.
Case 3: ,
,
,
and average of these values is 4.00.
