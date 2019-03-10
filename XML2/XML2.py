You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as .

Input Format

The first line contains , the number of lines in the XML document. 
The next  lines follow containing the XML document.

Output Format

Output a single line, the integer value of the maximum level of nesting in the XML document.

Sample Input

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
Sample Output

1
Explanation

Here, the root is a feed tag, which has depth of . 
The tags title, subtitle, link and updated all have a depth of . 

Thus, the maximum depth is .
