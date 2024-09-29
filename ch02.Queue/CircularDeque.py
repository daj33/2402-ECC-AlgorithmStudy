from ArrayQueue import ArrayQueue

class CircularDeque(ArrayQueue):
    #생성자 상속X
    def __init__(self, capacity=10):
        super.__init__(capacity)

    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): self.dequeue()
    def getFront(self): self.peek()

    def addFront(self, item):
        if self.isFull():
            pass
        else :
            self.array[self.front]=item
            self.front=(self.front-1)%self.capacity
    def deleteRear(self):
        if self.isEmpty():
            item = self.array[self.rear]
            self.rear=(self.rear-1)%self.capacity
            return item
    def getRear(self):
        if self.isEmpty():
            pass
        else :
            return self.array[self.rear]

