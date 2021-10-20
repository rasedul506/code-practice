# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slowPtr = fastPtr = head
        
        while (slowPtr and fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            
            if slowPtr == fastPtr: return True
        return False
