# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convertToNumber(self,l1: ListNode):
        nums = ''
        while l1:
            nums = str(l1.val) + nums
            l1 = l1.next
        return int(nums)      
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        l3 = head
        if l1: num1 = self.convertToNumber(l1)
        if l2: num2 = self.convertToNumber(l2)
        
        num3 = num1 + num2
        if num3 == 0: return head
        while num3 > 0:
            rem = num3 % 10
            num3 = num3 // 10
            newNode = ListNode(rem)
            l3.next = newNode
            l3 = l3.next
        return head.next
            
