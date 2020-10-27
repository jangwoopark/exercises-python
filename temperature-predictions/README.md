Objective
In this challenge, we practice predicting values. Check out the Resources tab for some tips on approaching this problem.

Task
Given a record containing the maximum and minimum monthly temperatures at a particular station. The record shows the temperature information for each month in a data range from  to ; however, some of the temperature values have been blanked out! Estimate and print the missing values.

Input Format

The first line contains an integer, , denoting the number of rows of data in the input file.
The second line contains the header for the tab-separated file; this line can be ignored, and is simply there to make the test case easier to read.
The  subsequent lines each describe the respective , , , and  data as a row of tab-separated values. In some of the rows, The  or  temperature field has been blanked out and replaced by: , , etc.

Constraints

Scoring

The score seen upon hitting  is the score against the sample test case (of  rows) only. It is normalized and will always lie between  and .
Upon hitting , the score seen is determined solely on the basis of the hidden test case.

Details on the Scoring Formula

We compute the average of the magnitude of difference between your predicted value and the actual recorded value for each of the missing terms. If this average exceeds  degrees, you will be assigned a score of zero.

For each of the values predicted by you (), we will compute an . The  is the difference of the predicted value () and the actual temperature at that location. Hence,


We will compute the average of all these error terms over all rows of data in the input file, and record it as 

Your score for this challenge will be 
Here, .

Output Format

Print each missing value on a new line.

Sample Input

20
yyyy    month   tmax    tmin
1908    January 5.0 -1.4
1908    February    7.3 1.9
1908    March   6.2 0.3
1908    April   Missing_1   2.1
1908    May Missing_2   7.7
1908    June    17.7    8.7
1908    July    Missing_3   11.0
1908    August  17.5    9.7
1908    September   16.3    8.4
1908    October 14.6    8.0
1908    November    9.6 3.4
1908    December    5.8 Missing_4
1909    January 5.0 0.1
1909    February    5.5 -0.3
1909    March   5.6 -0.3
1909    April   12.2    3.3
1909    May 14.7    4.8
1909    June    15.0    7.5
1909    July    17.3    10.8
1909    August  18.8    10.7  
The above test case is for explanatory purposes only, which is why we included only  lines.
The sample test case, which is run upon hitting , has  rows of data.
The hidden test case, which is used at the time of submission, has over  rows of data. The sample test case rows are a subset of it.

Sample Output

The four missing values (, , , and ) are:

8.6
15.8
18.9
0.0    
Your task is to predict values as close as possible to these.
