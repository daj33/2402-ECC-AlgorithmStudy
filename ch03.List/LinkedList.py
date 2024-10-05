class Node:
    def __init__(self, elem, link=None):
        self.data=elem
        self.link=link
    
    def append(self, node):
        if node is not None:
            node.link=self.link
            self.link=node

    def popNext(self):
        next= self.link
        if next is not None:
            self.link=next.link
        return next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head==None
    
    def isFull(self):
        return False
    
    def getNode(self, pos):
        if pos < 0: return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr
    
    def getEntry(self, pos):
        node=self.getNode(pos)
        if node==None: return None
        else: return node.data
    
    def insert(self, pos, e):
        node = Node(e, None)
        pre=self.getNode(pos-1)
        if pre==None:
            node.link = self.head
            self.head = node
            #이전 노드가 None라는 것은 리스트의 맨 앞에 추가하는 것으로 간주한다
        else: pre.append(node)

    def delete(self, pos):
        pre=self.getNode(pos-1)
        if pre==None:
            pre = self.head
            if self.head is not None:
                self.head = self.head.link
            return pre
        else: return pre.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr.link is not None:
            ptr = ptr.link
            count+=1
        return count
    
    def display(self, msg='Linked List: '):
        print(msg, end="")
        ptr = self.head
        while ptr.link is not None:
            print(ptr.data, end="-> ")
            ptr = ptr.link
        print('None')



