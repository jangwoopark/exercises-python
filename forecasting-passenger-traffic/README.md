Given an airport's total monthly passenger counts for a period of  months, forecast its passenger count for the next  months.

Input Format

The first line contains an integer, , denoting the number of months of passenger data. The  subsequent lines each contain the monthly passenger counts in the form of  tab-separated values:

The first value is , where  is an an integer denoting the month number.
The second value is an integer denoting the number of passengers for that month.
Scoring

The final score obtained upon submitting your code is solely dependent on the hidden test case. We will compute the mean of the magnitude of the percentage difference by comparing your expected answers with the actual sessions for each of the missing records in all test cases (samples included).

 (for all forecasted values in all test cases).

Your final score on a scale of  will be: 

If the mean value of  exceeds  (i.e.: your predictions are off by  or more on average), you will score zero. If your predictions are right on target, you will score .

When you hit  (instead of submit), we will run your solution against the sample test only. At that time, the visible score will be normalized out of  rather than . In case your program throws an error (or has an incorrect output format) for a single test case, the overall score assigned will be zero.

You may make no more than 15 submissions for this problem, during the contest.

Constraints


Output Format

For each line  (where ), print the forecasted passenger count for month number  on a new line.

Sample Input

The following is a truncated version of the first Test Case:

60
MonthNum_1  1226800
MonthNum_2  926891
MonthNum_3  782725
MonthNum_4  1023038
MonthNum_5  1126293
MonthNum_6  692565
MonthNum_7  1165880
MonthNum_8  1207156
MonthNum_9  1129954
MonthNum_10 745100
MonthNum_11 1059346
MonthNum_12 1168555
MonthNum_13 1317458
MonthNum_14 528045
MonthNum_15 1220238
MonthNum_16 874557
MonthNum_17 1033389
MonthNum_18 1034165
MonthNum_19 812094
MonthNum_20 1351419
MonthNum_21 801822
MonthNum_22 1044266
MonthNum_23 722871
MonthNum_24 742100
MonthNum_25 839471
MonthNum_26 1201199
MonthNum_27 796265
MonthNum_28 953887
MonthNum_29 1124602
MonthNum_30 1070181
MonthNum_31 1160366
MonthNum_32 1131150
MonthNum_33 1151813
MonthNum_34 1065316
MonthNum_35 914800
MonthNum_36 1093034
MonthNum_37 937898
MonthNum_38 991612
MonthNum_39 865649
MonthNum_40 990565
MonthNum_41 965414
MonthNum_42 949248
MonthNum_43 1168905
MonthNum_44 593112
MonthNum_45 1156922
MonthNum_46 870095
MonthNum_47 1023262
MonthNum_48 788327
MonthNum_49 543605
MonthNum_50 510786
MonthNum_51 734714
MonthNum_52 1133025
MonthNum_53 1461091
MonthNum_54 635481
MonthNum_55 1104107
MonthNum_56 844960
MonthNum_57 1271967
MonthNum_58 574319
MonthNum_59 1063900
MonthNum_60 724737
Sample Output

1563178
1312558
1312558
1388316
1325942
1312550
587396
1293945
1061128
590392
1092215
1446327
Explanation

The  printed lines of output are the forecasted passenger counts for the  months following month  (i.e.:  through .
