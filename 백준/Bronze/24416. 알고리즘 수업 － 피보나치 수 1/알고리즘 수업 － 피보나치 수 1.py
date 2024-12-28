n = int(input())
ex1 = 0
ex2 = 0

# 순환 함수
def fib_non_leaf(n):
    global ex1
    if n < 3:
        ex1 += 1  # 함수 호출 횟수 증가
        return 1
    else:
        return fib_non_leaf(n - 1) + fib_non_leaf(n - 2)

# Bottom-Up 메모이제이션
def fib_mem(n):
    global ex2
    if n < 3:  # n이 1 또는 2일 경우
        return 1
    mem = [0] * (n + 1)
    mem[1] = 1
    mem[2] = 1
    for i in range(3, n + 1):
        ex2 += 1  # 함수 호출 횟수 증가
        mem[i] = mem[i - 1] + mem[i - 2]
    return mem[n]

# 함수 호출
fib_non_leaf(n)  # 순환 방식
fib_mem(n)       # Bottom-Up 메모이제이션

# 호출 횟수 출력
print(ex1, end=' ')
print(ex2)


