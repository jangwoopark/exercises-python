This question is designed to help you get a better understanding of basic heap operations.
You will be given queries of  types:

" " - Add an element  to the heap.
" " - Delete the element  from the heap.
"" - Print the minimum of all the elements in the heap.
NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

Input Format

The first line contains the number of queries, .
Each of the next  lines contains a single query of any one of the  above mentioned types.

Constraints


Output Format

For each query of type , print the minimum value on a single line.

Sample Input

5  
1 4  
1 9  
3  
2 4  
3  
Sample Output

4  
9 
Explanation

After the first  queries, the heap contains {}. Printing the minimum gives  as the output. Then, the  query deletes  from the heap, and the  query gives  as the output.
