Jim runs a big burger restaurant and, to entertain his customers, he always tell them jokes. He is running out of jokes and he needs you to help him find new ones.

An often heard programmer joke goes like this:

"Why do programmers always mix up Christmas and Halloween? Because Dec 25 is Oct 31".

Got it? :-) It is because  (25 in Decimal) is equal to  (31 in Octal).

If we are talking about dates, then let  be the month and  be the date and the corresponding value be  ( in base ). Let's describe some slightly different jokes:

"Why do programmers always mix up event  and event ? Because ".

Here  means the month of event  and  the day of event . Similar for  and .

Jim knows that his customers love this kind of jokes. That's why he gives you a calendar with  events in it and asks you to count the number of such jokes he can create using the given events.

Two jokes ( and ) differ if they don't contain the same events.

Note:

The given numbers are all represented with digits from 0-9, that's why for months like  or , we can't use additional characters to represent 10 or 11.

It might happen, that a special event cannot be used for a joke because the base conversion is invalid. For example  is not possible since base  can only contain digits  and .

Unary base is invalid.

Two events can have the same date.

Input Format

On the first line you will get . The following  lines you will be given the dates ,  of the special events, each separated by a single space.

Output Format

Print the number of jokes Jim can make.

Constraints

(, ) will be a valid date in the Gregorian Calendar without leap day.
Sample Input #1

2
10 25
8 31
Sample Output #1

1
Sample Input #2

2
2 25
2 25
Sample Output #2

0
Sample Input #3

2
11 10
10 11
Sample Output #3

1
Explanation

There are two special events happening on  and . He can make one joke, namely the one described in the description.

In the second test case there are no valid dates we can use for our jokes since 25 is not defined for base 2.

In the third test case .
