import os
import sys

def strangeGrid(r, c):
    
    return ((r-(r%2==0))//2*10+(r%2==0)+(c-1)*2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
