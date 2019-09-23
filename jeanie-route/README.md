Byteland has  cities (numbered from  to ) and  bidirectional roads. It is guaranteed that there is a route from any city to any other city.

Jeanie is a postal worker who must deliver  letters to various cities in Byteland. She can start and end her delivery route in any city. Given the destination cities for  letters and the definition of each road in Byteland, find and print the minimum distance Jeanie must travel to deliver all  letters.

Note: The letters can be delivered in any order.

Input Format

The first line contains two space-separated integers,  (the number of cities) and  (the number of letters), respectively.
The second line contains  space-separated integers describing the delivery city for each letter.
Each line  of the  subsequent lines contains  space-separated integers describing a road as , where  is the distance (length) of the bidirectional road between cities  and .

Constraints

Output Format

Print the minimum distance Jeanie must travel to deliver all  letters.

Sample Input 0

5 3
1 3 4
1 2 1
2 3 2
2 4 2
3 5 3
Sample Output 0

6
Explanation 0

Jeanie has  letters she must deliver to cities , , and  in the following map of Byteland:jub1.png

One of Jeanie's optimal routes is , for a total distanced traveled of . Thus, we print  on a new line.
