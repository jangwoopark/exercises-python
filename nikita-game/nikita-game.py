import bisect
def dep(nums,start,end):
    sum ,temp= 0,0
    if(end<=start):
        return 0
    sum = nums[end]-nums[start-1]
    if sum%2==1:
        return 0
    if sum==0: #if numbers are all zeros, just return the list's length-1
        return end-start
    mid = sum/2+nums[start-1]
    left = bisect.bisect_left(nums,mid,start,end+1)
    if nums[left]!=mid:
        return 0
    return 1+max(dep(nums,start,left),dep(nums,left+1,end))


for _ in range(int(input().strip())):
    n = int(input().strip())
    nums = list(map(int,input().split(' ')))
    data = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        data[i] = data[i - 1] + nums[i - 1]
    print(dep(data,1,len(nums)))
