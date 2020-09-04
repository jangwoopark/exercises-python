def setbit(val, i, bit):

    num = 1 << i

    if bit:
        return val | num

    return val & ~num

n, q = map(int, input().strip().split(' '))
a = int(input().strip(),2)
b = int(input().strip(),2)
out = ''

for i in range(q):

    cmd = input().strip().split(' ')
    inx = int(cmd[1])
    cmd.append(7)
    bit = int(cmd[2])

    if cmd[0] =='set_a':

        a = setbit(a, inx, bit)

    elif cmd[0] =='set_b':

        b = setbit(b, inx, bit)

    else:

        c = a+b
        cbit = int (bool (c & (1<<inx)))
        out += str(cbit)

print (out)
