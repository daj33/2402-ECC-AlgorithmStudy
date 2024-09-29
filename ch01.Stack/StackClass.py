class ArrayStack:
    def __init__(self, capacity): 
        """
        self
        생성자를 포함해 클래스의 모든 멤버함수의 첫번째 매개변수
        자기자신(this: in java)을 의미한다
        """
        self.capacity= capacity
        self.array=[None]*self.capacity
        self.top=-1

    def isEmpty(self) :
       return self.top == -1

    def isFull(self):
        return self.top == self.capacity-1

    def push(self, item):
        if not self.isFull:
            self.top+=1
            self.array[self.top]=item
        else: pass

    def pop(self):
        if not self.isEmpty: 
            self.top-=1
            return self.array[self.top+1]
        else: pass

    def peek(self):
        if not self.isEmpty: 
            return self.array[self.top]
        else: pass
    
    def size(self):
        return self.top+1 #왜 책에서는 self를 사용하지 않았나? p.33
