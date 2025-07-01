import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a==0 and b==0 and c==0:
        break

    lst = sorted([a,b,c])

    if lst[2]**2 == lst[0]**2 + lst[1]**2:
        print("right")
    else:
        print("wrong") 
