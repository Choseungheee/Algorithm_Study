a, b, c, d, e, f = map(int, input().split())
x = (c*e - f*b)/(a*e - d*b)
if b!= 0:
    y = c/b - (a*x)/b
else:
    y = f/e - (d*x)/e
print(int(x), int(y))