from collections import deque

n, k = map(int, input().split())
q=deque(range(1, n+1))


while(len(q)>=k):
    q.rotate(-1)
    for i in range (k-1):
        q.popleft()

print(q[0])
