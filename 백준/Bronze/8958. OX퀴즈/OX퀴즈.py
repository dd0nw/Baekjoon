a = int(input())

for _ in range(a):
    lst = list(input())
    score = 0
    fn_score = 0
    for i in lst:
        if i == 'O':
            score += 1
            fn_score += score
        else:
            score = 0
    print(fn_score)