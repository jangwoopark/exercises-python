A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. Longest common subsequence (LCS) of 2 sequences is a subsequence, with maximal length, which is common to both the sequences.

Given two sequences of integers,  and , find the longest common subsequence and print it as a line of space-separated integers. If there are multiple common subsequences with the same maximum length, print any one of them.

In case multiple solutions exist, print any of them. It is guaranteed that at least one non-empty common subsequence will exist.

Recommended References

This Youtube video tutorial explains the problem and its solution quite well.


Function Description

Complete the longestCommonSubsequence function in the editor below. It should return an integer array of a longest common subsequence.

longestCommonSubsequence has the following parameter(s):

a: an array of integers
b: an array of integers
Input Format

The first line contains two space separated integers  and , the sizes of sequences  and .
The next line contains  space-separated integers .
The next line contains  space-separated integers .

Constraints





Constraints



Output Format

Print the longest common subsequence as a series of space-separated integers on one line. In case of multiple valid answers, print any one of them.

Sample Input

5 6
1 2 3 4 1
3 4 1 2 1 3
Sample Output

1 2 3
Explanation

There is no common subsequence with length larger than 3. And "1 2 3", "1 2 1", "3 4 1" are all correct answers.
