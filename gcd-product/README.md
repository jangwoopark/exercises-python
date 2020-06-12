This time your assignment is really simple.

Calculate GCD(1, 1) * GCD(1, 2) * ... * GCD(1, M) * GCD(2, 1) * GCD(2, 2) * ... * GCD(2, M) * ... * GCD(N, 1) * GCD(N, 2) * ... * GCD(N, M).

where GCD is defined as the Greatest Common Divisor.

Input Format

The first and only line contains two space separated integers N and M.

Output Format

Output the required product modulo 109+7.

Constraints

1 <= N, M <= 1.5 * 107

Sample input:

4 4
Sample output:

96
Explanation

For the above testcase, N = 4, M = 4. So,

GCD(1, 1) * GCD(1, 2) * ...... * GCD(4, 4) = 1 * 1 * 1 * 1 * 1 * 2 * 1 * 2 * 1 * 1 * 3 * 1 * 1 * 2 * 1 * 4 = 96.
