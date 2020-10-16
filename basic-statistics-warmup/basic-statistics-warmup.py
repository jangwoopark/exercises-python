n=int(input())
l = list(map(int, input().split()))

# AVERAGE---------------------------------
def avg(x):
    return sum(x)/len(x)

avg=avg(l)

# MEDIAN----------------------------------
l=sorted(l)   # List needs to be sorted
if len (l)%2 !=0:
    med=l[int((len(l)-1)/2)]
else:
    a=int(len(l)/2)
    b=a-1
    med=(l[a]+l[b])/2

# MODE-------------------------------------
def mode(list):   
    return max(list, key = list.count) 

# STANDARD DEVIATION------------------------
sum_squared=0
for i in l: 
    sum_squared=sum_squared+(i-avg)**2
sd=(sum_squared/len(l))**0.5

# CONFIDENCE INTERVALS ---------------------
    
lower_confidence = avg-1.96*sd/len(l)**0.5
upper_confidence = avg+1.96*sd/len(l)**0.5

# OUTPUT -----------------------------------
print('{:.1f}'.format(avg))
print('{:.1f}'.format(med))
print(mode(l))
print('{:.1f}'.format(sd))
print('{:.1f}'.format(lower_confidence), '{:.1f}'.format(upper_confidence))
