from  ArrayQueue import ArrayQueue

q = ArrayQueue(8)
q.display("초기상태")
for i in range(5):
    q.enqueue_ring(i)
q.display("0~4 삽입")

q.enqueue_ring(5)
q.enqueue_ring(6)
q.display("5,6 삽입 --> 포화상태")

q.enqueue_ring(8)
q.display("8 삽입 --> 0 삭제")
q.enqueue_ring(9)
q.display("9 삽입 --> 1 삭제")
