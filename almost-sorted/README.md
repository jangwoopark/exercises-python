Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.

Swap two elements.
Reverse one sub-segment.
Determine whether one, both or neither of the operations will complete the task. If both work, choose swap. For instance, given an array  either swap the  and , or reverse them to sort the array. Choose swap. The Output Format section below details requirements.

Function Description

Complete the almostSorted function in the editor below. It should print the results and return nothing.

almostSorted has the following parameter(s):

arr: an array of integers
Input Format

The first line contains a single integer , the size of .
The next line contains  space-separated integers  where .

Constraints



All  are distinct.

Output Format

If the array is already sorted, output yes on the first line. You do not need to output anything else.

If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

a. If elements can be swapped,  and , output swap l r in the second line.  and  are the indices of the elements to be swapped, assuming that the array is indexed from  to .

b. Otherwise, when reversing the segment , output reverse l r in the second line.  and  are the indices of the first and last elements of the subsequence to be reversed, assuming that the array is indexed from  to .

 represents the sub-sequence of the array, beginning at index  and ending at index , both inclusive.

If an array can be sorted by either swapping or reversing, choose swap.

If you cannot sort the array either way, output no on the first line.
Sample Input 1

2  
4 2  
Sample Output 1

yes  
swap 1 2
Explanation 1

You can either swap(1, 2) or reverse(1, 2). You prefer swap.

Sample Input 2

3
3 1 2
Sample Output 2

no
Explanation 2

It is impossible to sort by one single operation.

Sample Input 3

6
1 5 4 3 2 6
Sample Output 3

yes
reverse 2 5
Explanation 3

You can reverse the sub-array d[2...5] = "5 4 3 2", then the array becomes sorted.
