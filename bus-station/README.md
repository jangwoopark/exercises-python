There are  groups of friends, and each group is numbered from 1 to . The th group contains  people.

They live near a bus stop, and only a single bus operates on this route. An empty bus arrives at the bus stop and all the groups want to travel by the bus.

However, group of friends do not want to get separated. So they enter the bus only if the bus can carry the entire group.

Moreover, the groups do not want to change their relative positioning while travelling. In other words, group 3 cannot travel by bus, unless group 1 and group 2 have either (a) already traveled by the bus in the previous trip or (b) they are also sitting inside the bus at present.

You are given that a bus of size  can carry  people simultaneously.

Find the size  of the bus so that (1) the bus can transport all the groups and (2) every time when the bus starts from the bus station, there is no empty space in the bus (i.e. the total number of people present inside the bus is equal to )?

Input Format
The first line contains an integer  . The second line contains  space-separated integers  .

Output Format

Print all possible sizes of the bus in an increasing order.

Sample Input

8
1 2 1 1 1 2 1 3
Sample Output

3 4 6 12
Sample Explanation

In the above example,  = 1,  = 2,  = 1,  = 1,  = 1,  = 2,  = 1,  = 3.

If x = 1 : In the first trip,  go by the bus. There will be no second trip because the bus cannot accommodate group 2. Hence "x = 1" is not the required answer.

If x = 2 : No bus trip is possible. That's because  cannot go alone, as one seat will be left vacant in the bus. And,  &  cannot go together, because the bus is cannot accommodate both the groups simultaneously.

If x = 3 : In the first trip,  &  go by the bus. In the second trip, ,  &  go by the bus. In the third trip,  &  go by the bus. In the fourth trip,  go by the bus.

If x = 4 : In the first trip, ,  &  go by the bus. In the second trip, ,  & go by the bus. In the third trip,  &  go by the bus.

Similarly you can figure out the output for x= 5, 6 & 7.
