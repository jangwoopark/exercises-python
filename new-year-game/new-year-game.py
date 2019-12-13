import math
import os
import random
import re
import sys


if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        # Write Your Code Here
        new_arr=[x%3 for x in a]
        n_1=new_arr.count(1)
        n_2=new_arr.count(2)
        print('Balsa') if (n_1&1)|(n_2&1) else print('Koca')
