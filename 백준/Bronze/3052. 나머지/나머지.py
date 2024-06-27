A = []
for _ in range(10):
    A.append(int(input()))

B = []
for i in range(len(A)):
    B.append(A[i] % 42)

C = len(set(B))
print(C)
