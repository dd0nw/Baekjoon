import sys

T = int(sys.stdin.readline())
C=[]

for i in range(T):
    A,B = map(int, sys.stdin.readline().split())
    C.append(A+B)

for k in C:
    print(k)