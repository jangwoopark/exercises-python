You have N soldiers numbered from 1 to N. Each of your soldiers is either a liar or a truthful person. You have M sets of information about them. Each set of information tells you the number of liars among a certain range of your soldiers. Let L be the total number of your liar soldiers. Since you can't find the exact value of L, you want to find the minimum and maximum value of L.

Input Format

The first line of the input contains two integers N and M.
Each of next M lines contains three integers:
A B C where the set of soldiers numbered as {A, A+1, A+2, ..., B}, exactly C of them are liars. (1 <= Ai <= Bi <= n) and (0 <= Ci <= Bi-Ai).
Note: N and M are not more than 101, and it is guaranteed the given informations is satisfiable.

Output Format
Print two integers Lmin and Lmax to the output.

Sample Input #1

3 2
1 2 1
2 3 1
Sample Output #1

1 2
Sample Input #2

20 11
3 8 4
1 9 6
1 13 9
5 11 5
4 19 12
8 13 5
4 8 4
7 9 2
10 13 3
7 16 7
14 19 4
Sample Output #2

13 14
Explanation
In the first input, the initial line is "3 2", i.e. that there are 3 soldiers and we have 2 sets of information. The next line says there is one liar in the set of soldiers {1, 2}. The final line says there is one liar in the set {2,3}. There are two possibilities for this scenario: Soldiers number 1 and 3 are liars or soldier number 2 is liar.
So the minimum number of liars is 1 and maximum number of liars is 2. Hence the answer, 1 2.
