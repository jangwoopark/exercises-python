We define a modified Fibonacci sequence using the following definition:

Given terms  and  where , term  is computed using the following relation:

For example, if  and ,

,
,
,
and so on.
Given three integers, , , and , compute and print the  term of a modified Fibonacci sequence.

Function Description

Complete the fibonacciModified function in the editor below. It must return the  number in the sequence.

fibonacciModified has the following parameter(s):

t1: an integer
t2: an integer
n: an integer
Note: The value of  may far exceed the range of a -bit integer. Many submission languages have libraries that can handle such large results but, for those that don't (e.g., C++), you will need to compensate for the size of the result.

Input Format

A single line of three space-separated integers describing the respective values of , , and .

Constraints

 may far exceed the range of a -bit integer.
Output Format

Print a single integer denoting the value of term  in the modified Fibonacci sequence where the first two terms are  and .

Sample Input

0 1 5
Sample Output

5
Explanation

The first two terms of the sequence are  and , which gives us a modified Fibonacci sequence of . Because , we return the  term.
