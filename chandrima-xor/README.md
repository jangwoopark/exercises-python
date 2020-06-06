Chandrima likes the XOR operation very much and keeps finding and solving related problems. One day she comes across a problem and gets stuck on it, which makes her sad. You being her friend decide to help her out by writing a code for the same.

Consider a list of all natural numbers. Now you remove all numbers whose binary representation has at least two consecutive  bits, from the list, hence generating a new list having elements  and so on. Now you are given  numbers from this newly generated list. You have to find the XOR of these numbers.

Input Format
The first line has an integer , denoting the number of integers in list .
The next line contains  space-separated integers.  represents the  number of the generated list. Since the answer can be very large, print the answer modulo .

Output Format
Just print one line containing the final answer.

Constraints


Sample Input 1

3
1 2 3
Sample Output 1

7
Sample Input 2

3
1 3 4
Sample Output 2

0
Explanation

Sample 1:
The values to be considered are , and the answer is .

Sample 2:
The values to be considered are , and the answer is .
