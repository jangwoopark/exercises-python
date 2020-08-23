An XOR operation on a list is defined here as the xor () of all its elements (e.g.: ).

The  of set  is defined here as the sum of the s of all non-empty subsets of  known as . The set  can be expressed as:


For example: Given set 

The set of possible non-empty subsets is: 

The  of these non-empty subsets is then calculated as follows:
 = 

Given a list of  space-separated integers, determine and print .

For example, . There are three possible subsets, . The XOR of , of  and of . The XorSum is the sum of these:  and .

Note: The cardinality of powerset is , so the set of non-empty subsets of set  of size  contains  subsets.

Function Description

Complete the xoringNinja function in the editor below. It should return an integer that represents the XorSum of the input array, modulo .

xoringNinja has the following parameter(s):

arr: an integer array
Input Format

The first line contains an integer , the number of test cases.

Each test case consists of two lines:
- The first line contains an integer , the size of the set .
- The second line contains  space-separated integers .

Constraints




Output Format

For each test case, print its  on a new line. The  line should contain the output for the  test case.

Sample Input 0

1
3
1 2 3
Sample Output 0

12
Explanation 0

The input set, , has  possible non-empty subsets: .

We then determine the  of each subset in :







Then sum the results of the  of each individual subset in , resulting in  and .

Sample Input 1

2
4
1 2 4 8
5
1 2 3 5 100
Sample Output 1

120
1648
