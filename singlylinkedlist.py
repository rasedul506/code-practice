class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def length(self) -> int:
        length = 0
        cur = self.head

        while cur:
            length += 1
            cur = cur.next
        return length
    def display(self) -> list:
        cur = self.head
        element = []

        while cur:
            element.append(cur.data)
            cur = cur.next
        return element
    
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
    
    def prepend(self, data: int = None) -> None:
        if not data: return
        newNode = Node(data)
        cur = self.head

        newNode.next = cur
        self.head = newNode
    
    def remove(self, data: int = None) -> None:
        if not data: return
        cur = self.head

        if cur == self.head and cur.data == data:
            self.head = cur.next
            cur.next = None
            cur = None
            return
        while cur and cur.data != data:
            prev = cur
            cur = cur.next
        if not cur:
            return
        prev.next = cur.next
        cur = None
    
    def removeDuplicate(self, data: int = None) -> None:
        bucket = []
        cur = self.head

        while cur:
            if cur.data not in bucket:
                bucket.append(cur.data)
            else:
                prev.next = cur.next
                cur = None
                cur = prev
            prev = cur
            cur = cur.next

     

s = SinglyLinkedList()
print(s.display())
s.append(5)
s.prepend(9)
s.prepend(9)
print(s.display())
s.append(7)
print(s.display())
s.prepend(9)
s.prepend(11)
print(s.display())
print(s.length())
s.remove(5)
print(s.display())
print(s.length())
s.removeDuplicate()
print(s.display())
print(s.length())
