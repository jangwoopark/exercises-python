Li and Lu have  integers, , that they want to divide fairly between the two of them. They decide that if Li gets integers with indices  (which implies that Lu gets integers with indices ), then the measure of unfairness of this division is:

Find the minimum measure of unfairness that can be obtained with some division of the set of integers where Li gets exactly  integers.

Note  means Set complement

Input Format

The first line contains two space-separated integers denoting the respective values of  (the number of integers Li and Lu have) and  (the number of integers Li wants).
The second line contains  space-separated integers describing the respective values of .

Constraints

For  of the test cases, .
For  of the test cases, .
Output Format

Print a single integer denoting the minimum measure of unfairness of some division where Li gets  integers.

Sample Input 0

4 2
4 3 1 2
Sample Output 0

 6
Explanation 0
One possible solution for this input is . 

Sample Input 1

4 1
3 3 3 1
Sample Output 1

2
Explanation 1
The following division of numbers is optimal for this input: .
