from collections import deque

n, m = map(int, input().split(' '))
targets = map(int, input().split(' '))
dq = deque(range(1, n + 1))

cnt = 0
for target in targets:
    size = len(dq)
    goal = dq.index(target)
    if goal > size // 2: #등호가 들어가지 않는 이유: index는 0부터 시작한다!
        cnt += size - goal
        dq.rotate(size - goal) #양수: 시계방향 회전 
    else:
        cnt += goal
        dq.rotate(-goal)
    dq.popleft()
print(cnt)