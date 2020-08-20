Consider two non-negative long integers,  and , where . The bitwise AND of all long integers in the inclusive range between  and  can be expressed as , where  is the bitwise AND operator.

Given  pairs of long integers,  and , compute and print the bitwise AND of all natural numbers in the inclusive range between  and .

For example, if  and , the calculation is .

Function Description

Complete the andProduct in the editor below. It should return the computed value as an integer.

andProduct has the following parameter(s):

a: an integer
b: an integer
Input Format

The first line contains a single integer , the number of intervals to test.
Each of the next  lines contains two space-separated integers  and .

Constraints

Output Format

For each pair of long integers, print the bitwise AND of all numbers in the inclusive range between  and  on a new line.

Sample Input 0

3
12 15
2 3
8 13
Sample Output 0

12
2
8
Explanation 0

There are three pairs to compute results for:

 and 
, so we print  on a new line.
 and 
 and 
Sample Input 1

2
17 23
11 15
Sample Output 1

16
8
