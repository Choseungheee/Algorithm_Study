n, k = map(int, input().split())
lst = list(range(2, n+1))
cnt = 0
check = True
while check:
    p = lst[0]
    for i in lst:
        if i%p == 0:
            lst.remove(i)
            cnt += 1
        if cnt == k:
            print(i)
            check = False
            break