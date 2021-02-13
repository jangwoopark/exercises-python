You are given a sequence

. The task is to perform the following queries on it:

Type 1. Given two integers
and

. Reorder the elements of the sequence in such a way (changed part of the sequence is in brackets):
That is swap the first two elements of segment , the second two elements, and so on.

Type 2. Given two integers
and , print the value of sum

.

Input Format

The first line contains two integers
and . The second line contains integers

, denoting initial sequence.

Each of the next
lines contains three integers , where denotes the type of the query, and are parameters of the query. It's guaranteed that for a first-type query

will be even.

Constraints




Output Format

For each query of the second type print the required sum.

Sample Input

6 4
1 2 3 4 5 6
1 2 5
2 2 3
2 3 4
2 4 5

Example Output

5
7
9

Explanation

After the first query the sequence becomes [1, 3, 2, 5, 4, 6]. 
