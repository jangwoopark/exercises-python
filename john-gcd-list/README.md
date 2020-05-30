John is new to Mathematics and does not know how to calculate GCD of numbers. So he wants you to help him in a few GCD calculations. John has a list A of numbers, indexed 1 to N. He wants to create another list B having N+1 numbers, indexed from 1 to N+1, and having the following property:

GCD(B[i], B[i+1]) = A[i], ∀ 1 ≤ i ≤ N

As there can be many such lists, John wants to know the list B in which sum of all elements is minimum. It is guaranteed that such a list will always exist.

Input Format
The first line contains an integer T, i.e., the number of the test cases. T testcases follow.
The first line of each test case contains an integer N, i.e., the number of elements in the array.
The second line of each test case contains N space separated integers that denote the elements of the list A.

Output Format
For each test case, print in a new line the list B such that each element is separated by a single space.

Constraints
1 ≤ T ≤ 10
2 ≤ N ≤ 103
1 ≤ A[i] ≤ 104
1 ≤ B[i]

Sample Input

2
3
1 2 3
3
5 10 5
Sample Output

1 2 6 3
5 10 10 5
Explanation

For the first testcase,

 GCD(1,2) = 1
 GCD(2,6) = 2
 GCD(6,3) = 3
 sum = 1+2+6+3 = 12 which is minimum among all possible list B
For the second testcase,

GCD(5, 10) = 5
GCD(10, 10) = 10
GCD(10, 5) = 5
sum = 5 + 10 + 10 + 5 = 30 which is the minimum among all possible list B
