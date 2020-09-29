Watson gave a string  to Sherlock. It is  characters long and consists of only 1s and 0s. Now he asks: Given an integer , I'll pick two indices  and  at random between  and , both inclusive. What's the probability that both  and  are 1 and ?

Input Format
First line contains , the number of testcases. Each testcase consists of (the length of ) and  in one line and string in second line.

Output Format
Print the required probability as an irreducible fraction. If required answer is 0, output 0/1.

Constraints




Sample input

2
4 3
1011
4 1
1011
Sample output

9/16
5/16
Explanation
test1: Out of 16 choices, 9 pairs of  satisfy our condition.

(1,1), (1,3), (1,4), (3,1), (3,3), (3,4), (4,1), (4,3), (4,4)      
test2: Out of 16 choices, 5 pairs of  satisfy our condition.

(1,1), (3,3), (4,4), (4,3), (3,4)  
