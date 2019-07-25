from string import ascii_uppercase as aaa

def decode(k,m):
    # remove duplicates from key
    key = ''.join([x for i,x in enumerate(k) if k.index(x)==i])
    
    # get aplhabet w/o chars in key
    alph = ''.join([x for x in aaa if x not in key])
    
    # get base ordered char
    dec = key + alph
    
    # create columns by indexing: range() with steps of len(key) &
    # increasing start-value from 0 to len(key) + sort them 
    columns = sorted([''.join([dec[x] for x in
                               range(n,len(dec),len(key))])
                      for n in range(len(key))])
 
    # create decoding dict
    d = {a:b for b,a in zip(aaa,''.join(columns))}
    
    # decode
    return ''.join( d[x] if x in d else ' ' for x in m)    
    
for _ in range(int(input())):
    key = input()
    mes = input() 
    
    print(decode(key,mes))
