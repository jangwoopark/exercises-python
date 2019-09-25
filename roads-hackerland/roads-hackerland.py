
import sys
import collections
import heapq

sys.setrecursionlimit(1000000000)

graph=collections.defaultdict(dict)
answer=0
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

'''The below will update the distance to existing path only if the new path is lesser then the existing'''
for a1 in range(0,m):
        x,y,r = map(int,input().strip().split(' '))
        z = r
        if y in graph[x]: 
            if z <  graph[x][y]:
                graph[x][y] = z  
                graph[y][x] = z
            else:
                pass
            
        else:
            graph[x][y] = z  
            graph[y][x] = z
'''Counting the number of cities attached to each city'''           
def dfs(node,graph1,numcities):
    if node not in visited:
        visited[node]=1
        for vertex,weight in graph1[node].items():
            numcities[vertex]+=1
            dfs(vertex,graph1,numcities)
            
            
'''Building a MST here'''
heap=[];heapq.heappush(heap,(0,1));parent=[0]*(n+1) ; key = [sys.maxsize]*(n+1);key[1] = 0
Inmstset=set()
while heap :
    weight,node = heapq.heappop(heap)
    if node not in Inmstset:
        Inmstset.add(node)
        for node_c,weight_c in graph[node].items():
            if weight_c <  key[node_c] and  node_c not in Inmstset:
                key[node_c] = weight_c
                parent[node_c] = node
                heapq.heappush(heap,(weight_c,node_c))
               
'''Building a new graph with the new MST found'''         
graph1=collections.defaultdict(dict)
for i in range(2,n+1):
    graph1[parent[i]][i] = graph[parent[i]][i]  
    graph1[i][parent[i]] = graph[parent[i]][i] 
visited={}    
numcities=[0]*(n+1)
dfs(1,graph1,numcities)
answer=0
#long(answer)
visited={}
'''Going through each path and finding the distances'''
for i in range(1,n+1):
    for k,v in graph1[i].items():
        if (i,k) not in visited:
            visited[(i,k)]=1;visited[(k,i)]=1
            
            multfactor = min(numcities[i],numcities[k])
            multfactor_1 =  (multfactor*(n-multfactor))
            
            answer = answer +  multfactor_1*(1<<graph1[i][k])
            

print (bin(answer)[2:])
