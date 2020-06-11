You are currently studying the language  ( which means strange in English ) from a renowned professor. The language has infinite number of letters in its alphabet ( now you know, why it is called ajob ).

The professor taught you  words, one by one. The number of letters in a word is equal to it's place in the teaching order. Thus, the  word taught by the professor has  letter,  word has  letters,  word has  letters, , the  word has  letters.

All the letters within a word are distinct to each other.

Now, you are handed an assignment. You have to choose any one of the  words and form a subsequence from it. The length of the subsequence should be exactly  less than the length of original word. For example, if the length of the chosen word is , then the length of the subsequence should be . If for any word,  is smaller than  , then you must not choose that word. Two subsequences are different to each other if, the lengths of them are different or they contain different characters in the same position.

Find the number of ways you can complete the assignment  (  will always be a  ).

1.
The first line contains , the number of testcases. The next  lines contain three space separated integers ,  and .

Output Format
For each testcase, print one integer in a single line, the number possible ways you can complete the assignment, .

Constraints





Sample Input #00

3
2 1 2
2 1 5
5 3 13
Sample Output #00

1
3
2
Sample Input #01

5
5 2 3
6 5 11
7 6 3
6 5 7
6 5 5
Sample Output #01

2
7
2
0
2
