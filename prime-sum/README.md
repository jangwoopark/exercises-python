The problem is quite simple. You're given a number N and a positive integer K. Tell if N can be represented as a sum of K prime numbers (not necessarily distinct).

Input Format
The first line contains a single integer T, denoting the number of test cases.
Each of the next T lines contains two positive integers, N & K, separated by a single space.

Output Format
For every test case, output "Yes" or "No" (without quotes).

Constraints
1 <= T <= 5000
1 <= N <= 1012
1 <= K <= 1012

Sample Input

2
10 2
1 6
Sample Output

Yes
No
Explanation

In the first case, 10 can be written as 5 + 5, and 5 is a prime number. In the second case, 1 cannot be represented as a sum of prime numbers, because there are no prime numbers less than 1.
