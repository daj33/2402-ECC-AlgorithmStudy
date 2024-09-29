import queue

s1 = list()

msg = input("문자열 입력: ")
for c in msg:
    s1.append(c)

print("문자열 출력: ", end='')
#end: print() 함수에서 출력 후 끝에 추가할 문자열을 지정
while(len(s1)>0):
    print(s1.pop(), end='')
print()


s2= queue.LifoQueue(maxsize=20)

msg = input("문자열 입력: ")
for c in msg:
    s2.put(c)

print("문자열 출력: ", end='')
while not s2.empty():
    print(s2.get(), end='')
print()
