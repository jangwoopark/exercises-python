One day, Wet Shark was given an array . As always, he started playing with its subsequences.

When you came to know about this habit, you presented him a task of finding all pairs of subsequences, , which satisfies all of the following constraints. We will represent a pair of subsequence as  and 

 and  must be of same length, i.e., .
Please help Wet Shark determine how many possible subsequences  and  can exist. Because the number of choices may be big, output your answer modulo .

Note:

Two segments are different if there's exists at least one index  such that element  is present in exactly one of them.
Both subsequences can overlap each other.
Subsequences do not necessarily have to be distinct
Input Format

The first line consists of 3 space-separated integers , , , where  denotes the length of the original array, , and  and  are as defined above.
The next line contains  space-separated integers,  , representing the elements of .

Constraints

Output Format

Output total number of pairs of subsequences, , satisfying the above conditions. As the number can be large, output it's modulo 

Sample Input 0

4 5 3
1 1 1 4
Sample Output 0

3
Explanation 0

For array  there are three pairs of subsequences:

