import queue
import collections

q = queue.Queue(10)
dq = collections.deque()

for i in range(9):
    q.put(i)
    if i%2==0 :
        dq.append(i)
    else: dq.appendleft(i)

#queue: 0 1 2 3 4 5 6 7 8
while not q.empty():
    print(q.get(), end=' ')
print()

#deque: 7 5 3 1 2 4 6 8
print(dq.pop())
print(dq.pop())
print(dq.popleft())
print(dq.popleft())
print(dq.popleft())