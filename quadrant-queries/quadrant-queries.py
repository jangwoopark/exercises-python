n = int(input())
p_list = []
num_list = []
c_list=[]
cmd_list = []

for x in range (n):
    p_list = [int (x) for x in input().split()]
    num_list.append(p_list)
num_cmd = int(input())
for x in range(num_cmd):
    c_list = [x for x in input().split()]
    cmd_list.append(c_list)
for x in range(num_cmd):
    x_i = int(cmd_list[x][1])-1
    x_j = int(cmd_list[x][2])
    if(cmd_list[x][0]=='C'):
        first = 0
        second = 0
        third = 0
        fourth = 0
        for _ in range(x_i,x_j):
            if(num_list[_][0]>0 and num_list[_][1]>0):
                first = first + 1
            elif(num_list[_][0]<0 and num_list[_][1]>0):
                second = second + 1
            elif(num_list[_][0]<0 and num_list[_][1]<0):
                third = third + 1
            else:
                fourth = fourth + 1
        print(first,second,third,fourth)
    elif(cmd_list[x][0]=='X'):
        for _ in range(x_i,x_j):
            num_list[_][1] = -num_list[_][1]
    else:
        for _ in range(x_i,x_j):
            num_list[_][0] = -num_list[_][0]
