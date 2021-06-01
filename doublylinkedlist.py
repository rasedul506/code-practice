class Node:
    def __init__(self,data: int=None) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def length(self) -> int:
        length = 0
        cur = self.head

        while cur:
            length += 1
            cur = cur.next
        return length
    
    def display(self) -> None:
        element = []
        cur = self.head

        while cur:
            element.append(cur.data)
            cur = cur.next
        print(element)
    
    def append(self, data: int = None) -> None:
        if not data: return
        cur = self.head
        newNode = Node(data)
        if not cur:
            self.head = newNode
            return
        while cur.next:
            cur = cur.next
        cur.next = newNode
        newNode.prev = cur
    
    def prepend(self, data: int = None) -> None:
        if not data: return
        cur = self.head
        newNode = Node(data)

        if not cur:
            self.head = newNode
            return
        newNode.next = cur
        cur.prev = newNode
        self.head = newNode

    def remove(self, data: int = None) -> None:
        if not data: return
        cur = self.head
        if not cur: return

        while cur:
            if cur == self.head and cur.data == data:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    next = cur.next
                    next.prev = None
                    cur.next = None
                    cur = None
                    self.head = next
                    return
            if cur.data == data:
                if not cur.next:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                else:
                    prev = cur.prev
                    next = cur.next
                    prev.next = next
                    next.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next


    def removeDuplicate(self) -> None:
        bucket = []
        cur = self.head

        if not cur: return

        while cur:
            if cur.data not in bucket:
                bucket.append(cur.data)
            else:
                prev = cur.prev
                next = cur.next
                prev.next = next
                if next:
                    next.prev = prev
                cur.next = None
                cur.prev = None
                cur = None
                cur = prev
            cur = cur.next

d = DoublyLinkedList()
d.display()
d.append(5)
d.display()
d.append(4)
d.append(9)
d.display()
d.prepend(9)
d.display()
d.prepend(7)
d.display()
print('length: {}'.format(d.length()))
d.remove(4)
d.display()
d.removeDuplicate()
d.display()
