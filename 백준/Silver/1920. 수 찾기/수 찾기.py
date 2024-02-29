n=int(input())
A=list(map(int, input().split()))
A.sort()
m=int(input())
B=list(map(int, input().split()))

def binary_search(target, array):
    current_min = 0
    current_max = n-1
    cursor = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[cursor] == target:
            return 1
        elif array[cursor] < target:
            current_min = cursor + 1
        else:
            current_max = cursor -1

        cursor = (current_max + current_min) // 2
    return 0

for i in range(m):
    print(binary_search(B[i], A))