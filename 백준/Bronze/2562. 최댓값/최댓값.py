import sys
a=[]
for i in range(9):
    b=int(sys.stdin.readline())
    a.append(b)

print(max(a))
print(a.index(max(a))+1)