import sys

N = int(sys.stdin.readline())
a=[]
for i in range(N):
    a.append(list(map(int, sys.stdin.readline().split())))

a.sort()
for k in a:
    print(*k)
