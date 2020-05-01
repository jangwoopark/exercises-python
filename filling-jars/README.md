Animesh has  empty candy jars, numbered from  to , with infinite capacity. He performs  operations. Each operation is described by  integers, , , and . Here,  and  are indices of the jars, and  is the number of candies to be added inside each jar whose index lies between  and  (both inclusive). Can you tell the average number of candies after  operations?

Input Format

The first line contains two integers,  and , separated by a single space.
 lines follow; each of them contains three integers, , , and , separated by spaces.

Constraints




Output Format

A single line containing the average number of candies across  jars, rounded down to the nearest integer.

Note: Rounded down means finding the greatest integer which is less than or equal to the given number. E.g. 13.65 and 13.23 are rounded down to 13, while 12.98 is rounded down to 12.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

160
Explanation

Initially each of the jars contains 0 candies

0 0 0 0 0  
First operation:

100 100 0 0 0  
Second operation:

100 200 100 100 100  
Third operation:

100 200 200 200 100  
Total = 800, Average = 800/5 = 160
