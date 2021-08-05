n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False]*n
s = []
def solution(s, n, m):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    o = 0
    for i, a in enumerate(arr):
        if not visited[i] and o != arr[i]:
            visited[i] = True
            s.append(arr[i])
            o = arr[i]
            solution(s, n, m)
            visited[i] = False
            s.pop()
solution([], n, m)