for _ in range(eval(input())):
    n,a,b = input(),[int(i) for i in input().split()],0
    for j in a: 
        b ^= j
    if b == 0: 
        print ("Second")
    else: 
        print ("First")
