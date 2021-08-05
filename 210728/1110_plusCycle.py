n = int(input())
n1 = n%10
n10 = n//10
count = 0
s = n1+n10
while True:
    count += 1
    new = (n1*10)+(s%10)
    if new == n:
        break
    n1 = new%10
    n10 = new//10
    s = n1 + n10
print(count)