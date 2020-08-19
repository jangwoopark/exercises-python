Sansa has an array. She wants to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the values thus obtained. Determine this value.

For example, if :

Subarray	Operation	Result
3		None		3
4		None		4
5		None		5
3,4		3 XOR 4		7
4,5		4 XOR 5		1
3,4,5		3 XOR 4 XOR 5	2
Now we take the resultant values and XOR them together:


Function Description

Complete the sansaXor function in the editor below. It should return an integer that represents the results of the calculations.

sansaXor has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer , the number of the test cases.

Each of the next  pairs of lines is as follows:
- The first line of each test case contains an integer , the number of elements in .
- The second line of each test case contains  space-separated integers .

Constraints




Output Format

Print the results of each test case on a separate line.

Sample Input 0

2
3
1 2 3
4
4 5 7 5
Sample Output 0

2
0
Explanation 0

Test case 0:


Test case 1:

Sample Input 1

2
3
98 74 12
3
50 13 2
Sample Output 1

110
48
Explanation 1

Test Case 0:


Test Case 1:


