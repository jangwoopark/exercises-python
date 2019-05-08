N = int(input())
 
n = N % 2 

if n == 0 and (2<= N <=5): 
    print('Not Weird')
elif n == 0 and (6<= N <=20): 
    print('Weird')
elif n == 0 and N > 20: 
    print("Not Weird")
elif N % 2 != 0: 
    print('Weird')
