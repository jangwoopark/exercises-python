Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring .

In one step, Alice can change a  to a  or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

For example, if Alice's string is  she can change any one element and have a beautiful string.

Function Description

Complete the beautifulBinaryString function in the editor below. It should return an integer representing the minimum moves required.

beautifulBinaryString has the following parameter(s):

b: a string of binary digits
Input Format

The first line contains an integer , the length of binary string.
The second line contains a single binary string .

Constraints

.
Output Format

Print the minimum number of steps needed to make the string beautiful.

Sample Input 0

7
0101010
Sample Output 0

2  
Explanation 0:

In this sample, 

The figure below shows a way to get rid of each instance of :

binary.png

Because we were able to make the string beautiful by changing  characters ( and ), we print .

Sample Input 1

5
01100
Sample Output 1

0
Sample Case 1:

In this sample 

Explanation 1

The substring  does not occur in , so the string is already beautiful and we print .

Sample Input 2

10
0100101010
Sample Output 2

3
Explanation 2

In this sample 

One solution is to change the values of  to form a beautiful string.
