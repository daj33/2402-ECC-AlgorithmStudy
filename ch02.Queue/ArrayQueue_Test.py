from ArrayQueue import ArrayQueue
import random

q = ArrayQueue(11)

q.display("*초기상태")
while not q.isFull():
    q.enqueue(random.randint(0, 20))
q.display("*포화상태")

print("*삭제과정")
while not q.isEmpty():
    print(q.dequeue(), end=' 삭제\n')
    q.display("상태: ")
print()

