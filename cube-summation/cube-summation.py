T = int(input().strip())

for _ in range(T):
    N,M = list(map(int,input().strip().split()))
    base = dict()
    for _ in range(M):
		c = input().strip().split()
		if c[0] == "UPDATE":
			x,y,z,w = [int(p) for p in c[1:]]
			base[(x,y,z)] = w
		else: # c[0:5] == "QUERY":
			r = [int(p) for p in c[1:]]
			X,Y,Z = [range(r[i],r[i+3]+1) for i in range(3)]
			print(sum(base[(x,y,z)] for x,y,z in base if x in X and y in Y and z in Z))
