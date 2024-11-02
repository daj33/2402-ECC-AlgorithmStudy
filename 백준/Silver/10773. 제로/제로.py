from collections import deque

stack = deque()
n = int(input())
count = 0
value = 0
for i in range(n):
    e = int(input())
    if e==0 :
        stack.pop()
        count-=1
    else :
        stack.append(e)
        count+=1
for i in range(count):
    value += stack.pop()
print(value)
    