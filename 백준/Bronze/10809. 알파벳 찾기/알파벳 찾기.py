S = input()

for i in range(97, 123):
    a=chr(i)
    
    if a in S:
        print(S.index(a), end=' ')
    else:
        print(-1, end=' ')
