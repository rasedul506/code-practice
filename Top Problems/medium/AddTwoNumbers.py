# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convertToNumber(self,l1: ListNode):
        num = ''
        while l1:
            num = str(l1.val)+num
            l1=l1.next
        return int(num)
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        l3 = head
        num1=num2=0
        if l1: num1 = self.convertToNumber(l1)
        if l2: num2 = self.convertToNumber(l2)
        
        num3 = num1 + num2
        if num3 == 0:
            return head
        while num3 > 0:
            rem = num3%10
            num3 = num3//10
            newNode=ListNode(rem)
            l3.next = newNode
            l3 = l3.next
        return head.next
        
