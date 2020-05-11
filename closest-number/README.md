You are given 3 numbers a, b and x. You need to output the multiple of x which is closest to ab. If more than one answer exists , display the smallest one.

Input Format

The first line contains T, the number of testcases.
T lines follow, each line contains 3 space separated integers (a, b and x respectively)

Constraints

1 ≤ T ≤ 105
1 ≤ x ≤ 109
0 < ab ≤ 109
1 ≤ a ≤ 109
-109 ≤ b ≤ 109

Output Format

For each test case , output the multiple of x which is closest to ab

Sample Input 0

3
349 1 4
395 1 7
4 -2 2
Sample Output 0

348
392
0
Explanation 0

The closest multiple of 4 to 349 is 348.
The closest multiple of 7 to 395 is 392.
The closest multiple of 2 to 1/16 is 0.
