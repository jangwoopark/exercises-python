import math

mod = 10**9 + 7

def solve():
    m,r,s = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    print(number_of_subsequence_pairs(arr,r,s))

def number_of_subsequence_pairs(arr,r,s):
    target1 = r + s     # know for fact: target1 >= target2
    target2 = r - s
    m = len(arr)
    values = make_initial_value_set(arr,target1)
    arr.insert(0,0)     # 1-indexing
    memo = [[{} for j in range(m + 1)] for i in range(m + 1)]
    for j in range(1,m+1):
        for i in range(j,m + 1):
            s_range = calculate_sum_range(target1,values,i,j,memo)
            for s in s_range:
                count = count_subsequences(i,j,s,arr,memo)
                if count != 0:
                    memo[i][j][s] = count
    return combine_subsequence_pairs(target1,target2,memo,m)

def make_initial_value_set(arr,target):
    return set([i*2 for i in arr if i*2 <= target])

def calculate_sum_range(target,values,i,j,memo):
    if j == 1:
        return values
    elif len(memo[i][j-1]) > 0:
        return range(min(memo[i][j-1]),target + 1)
    else:
        return range(0)

def count_subsequences(i,j,s,arr,memo):
    if j == 1:
        if s == arr[i]*2:
            count = 1 + get_num_subsequences(i-1,j,s,memo)
        else:
            count = get_num_subsequences(i-1,j,s,memo)
    else:
        count = get_num_subsequences(i-1,j-1,s-(arr[i]*2),memo) + get_num_subsequences(i-1,j,s,memo)
    return count

def get_num_subsequences(i,j,s,memo): return memo[i][j].get(s,0)
    
def combine_subsequence_pairs(target1,target2,memo,m):
    result = 0
    for j in range(1,m+1):
        result += (memo[m][j].get(target1,0) * memo[m][j].get(target2,0)) % mod
        result %= mod
    return result
    
solve()
