N = int(input())
a=[]
for i in range(N):
    a.append(list(map(int, input().split())))
    
a.sort()

for k in a:
    print(*k)
