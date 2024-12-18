n1, m1 = map(int, input().split())  
A = []
for i in range(n1):
    A.append(list(map(int, input().split())))

n2, m2 = map(int, input().split())  
B = []
for i in range(n2):
    B.append(list(map(int, input().split())))

C = [[0] * m2 for _ in range(n1)]

for i in range(n1):
    for j in range(m2):
        for k in range(m1):
            C[i][j] += A[i][k] * B[k][j]
            
for row in C:
    print(*row)  # 행을 띄어쓰기로 출력
