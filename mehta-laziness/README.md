Mehta is a very lazy boy. He always sleeps in Maths class. One day his teacher catches him sleeping and tells him that she would mark him absent for the whole semester. While she pretends to be strict, she is actually very kind-hearted. So she wants to give Mehta a chance to prove himself. She gives him a problem. If Mehta can answer it correctly, she will forgive him. Can you help Mehta find the answer to this problem?

The problem: The teacher gives Mehta a number  and asks him to find out the probability that any proper divisor of  would be an even perfect square.

Note: Even perfect square means the number should be even and a perfect square.

Input Format
The first line of input contains an integer , the number of test cases.
 lines follow, each line containing , the number that the teacher provides.

Output Format
For each test case, print in a newline the output in  format where  and  are positive coprime integers.
if  is 0, you should simply output 0.

Constraints


Sample Input

4
2
8
36
900
Sample Output

0
1/3
1/8
3/26
Explaination
For the first case , the set of proper divisors is . Since  is not an even perfect square, the probability is .
For the second case , the set of proper divisors is  and only  is an even perfect square among them, so probability = .
For the third case , the set of proper divisors is , and only  is an even perfect square, so probability = .
For the fourth case , there will be total of  proper divisors and  of them  are even perfect squares.
