Given an array of stick lengths, use  of them to construct a non-degenerate triange with the maximum possible perimeter. Print the lengths of its sides as  space-separated integers in non-decreasing order.

If there are several valid triangles having the maximum perimeter:

Choose the one with the longest maximum side.
If more than one has that maximum, choose from them the one with the longest minimum side.
If more than one has that maximum as well, print any one them.
If no non-degenerate triangle exists, print -1.

For example, assume there are stick lengths . The triplet  will not form a triangle. Neither will  or , so the problem is reduced to  and . The longer perimeter is .

Function Description

Complete the maximumPerimeterTriangle function in the editor below. It should return an array of  integers that represent the side lengths of the chosen triangle in non-decreasing order.

maximumPerimeterTriangle has the following parameter(s):

sticks: an integer array that represents the lengths of sticks available
Input Format

The first line contains single integer , the size of array .
The second line contains  space-separated integers , each a stick length.

Constraints

Output Format

Print the lengths of the  chosen sticks as space-separated integers in non-decreasing order.

If no non-degenerate triangle can be formed, print -1.

Sample Input 0

5
1 1 1 3 3
Sample Output 0

1 3 3
Explanation 0

There are  possible unique triangles:

The second triangle has the largest perimeter, so we print its side lengths on a new line in non-decreasing order.

Sample Input 1

3
1 2 3
Sample Output 1

-1
Explanation 1

The triangle  is degenerate and thus can't be constructed, so we print -1 on a new line.

Sample Input 2

6
1 1 1 2 3 5
Sample Output 2

1 1 1
Explanation 2

The triangle (1,1,1) is the only valid triangle.
