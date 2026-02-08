# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Traversing the list and inserting in stack

        stack_l1, stack_l2 = [] , []
        while l1:
            stack_l1.append(l1.val)
            l1 = l1.next

        while l2:
            stack_l2.append(l2.val)
            l2 = l2.next

        #Build Numbers
        num1 , num2 = 0 , 0
        while stack_l1:
            num1 = num1 * 10 + stack_l1.pop()
        while stack_l2:
            num2 = num2 * 10 + stack_l2.pop()
        total = num1+num2


        #Handling edge case if total is 0
        if total == 0:
            return ListNode(0)
        
        dummyNode = ListNode(0)
        current = dummyNode
        while total > 0:
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            total//=10
        return dummyNode.next