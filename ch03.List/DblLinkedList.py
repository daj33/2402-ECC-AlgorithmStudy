class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next

    def append(self, node):
        if node is not None:
            node.prev = self
            node.next = self.next
            if node.next is not None:
                node.next.prev = node
            self.next = node
    
    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev=self
        return node

class DblLinkedList:
    def __init__(self):
        self.head = None
    
    #isFull(), isEmpty(), getEntry() 등 LinkedList와 코드가 정확히 동일함

    #getNode(), size(), display() 등 ptr.link 를 ptr.next로 수정하면 동일함

    def insert(self, pos, e):
        node = DNode(e)
        pre = self.getNode(pos-1)
        if pre==None: #첫번째 노드로 삽입한다 
            node.next = self.head
            if node.next is not None:
                node.next.pre = node
            self.head= None
        else: pre.append(node)

def delete(self, pos):
    pre = self.getNode(pos-1)
    if pre==None: #첫번째 노드를 삭제한다 
        pre=self.head
        if self.head is not None:
            self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        return pre
    else: pre.popNext()