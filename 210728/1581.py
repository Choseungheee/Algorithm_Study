from math import sqrt
m = int(input())
n = int(input())
s = 0
for i in range(m, n+1):
    if i == 2:
        s += i
        small = i
        continue
    if i < 2 or i%2 == 0:
        continue
    for j in range(2, int(sqrt(i))+1):
        if i%j == 0:
            break
    else:
        if s == 0:
            small = i
        s += i
if s == 0:
    print(-1)
else:
    print(s)
    print(small)