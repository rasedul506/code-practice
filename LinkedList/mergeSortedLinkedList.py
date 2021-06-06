## Merge two sorted linked lists and return it as a sorted list.
## The list should be made by splicing together the nodes of the first two lists.
## Input: l1 = [1,2,4], l2 = [1,3,4]
## Output: [1,1,2,3,4,4]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
