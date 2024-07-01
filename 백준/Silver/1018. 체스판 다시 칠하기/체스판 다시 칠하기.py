n, m= map(int, input().split())

mtr = []
cnt = []

for i in range(n):
    mtr.append(input())

for a in range(n-7):
    for b in range(m-7):
        w_idx=0
        b_idx=0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2==0:
                    if mtr[i][j]!='W':
                        w_idx+=1
                    else:
                        b_idx+=1
                else:
                    if mtr[i][j]!='W':
                        b_idx+=1
                    else:
                        w_idx+=1
        cnt.append(w_idx)
        cnt.append(b_idx)

print(min(cnt))