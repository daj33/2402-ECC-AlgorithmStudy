capacity = 10
array = [None]*capacity
top=-1 #가장 최근에 삽입한 요소의 인덱스 

"""
배열의 인덱스 -1 : 공백상태를 의미한다 
"""

def isEmpty() :
    if top==-1 : 
        return True
    else : 
        return False

def isFull():
    if top==capacity-1: 
        return True
    else : 
        return False

def push(e):
    if isFull : 
        print("stack overflow") 
        exit()
    else: 
        top += 1
        array[top] = e

def pop():
    if isEmpty: 
        print("stack underflow")
        exit()
    else: 
        top -= 1
        return array(top+1)

def peek():
    if isEmpty:
        pass #런타임 예외 무시
    else: 
        return array[top]
    
def size():
    return top+1