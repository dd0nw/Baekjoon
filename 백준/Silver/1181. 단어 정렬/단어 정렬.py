import sys

a = int(sys.stdin.readline())
lst=[]

for i in range(a):
    lst.append(sys.stdin.readline().strip())


set_lst=list(set(lst))
set_lst.sort()
set_lst.sort(key=len)

for j in set_lst:
    print(j)