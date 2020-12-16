st= []
maxArr = [0]
for _ in range(int(input())):
    x = input().split()
    if x[0]=='1':
        st.append(int(x[1]))
        if maxArr[-1]<=int(x[1]):
            maxArr.append(int(x[1]))
    elif x[0]=='2':
        if st.pop() == maxArr[-1]:
            maxArr.pop()
    elif x[0]=='3':
        print(maxArr[-1])
