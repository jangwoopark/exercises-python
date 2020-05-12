Sherlock is stuck while solving a problem: Given an array , he wants to know if there exists a subset  of this array which follows these statements:

 is a non-empty subset.
There exists no integer  which divides all elements of .
There are no elements of  which are equal to another.
Input Format

The first line of input contains an integer, , representing the number of test cases. Then  test cases follow.
Each test case consists of two lines. The first line contains an integer, , representing the size of array . In the second line there are  space-separated integers, , representing the elements of array .

Constraints



Output Format

Print YES if such a subset exists; otherwise, print NO.

Sample Input

3
3
1 2 3
2
2 4
3
5 5 5
Sample Output

YES
NO
NO
Explanation

In the first test case,  are all the possible non-empty subsets, of which the first and the last four satisfy the given condition.

For the second test case, all possible subsets are . For all of these subsets,  divides each element. Therefore, no non-empty subset exists which satisfies the given condition.

For the third test case, the following subsets exist: 123. Because the single element in the first subset is divisible by  and the other two subsets have elements that are equal to another, there is no subset that satisfies every condition.
