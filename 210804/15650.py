n,m = list(map(int,input().split()))
s = []
def combi(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            combi(i+1)
            s.pop()
combi(1)