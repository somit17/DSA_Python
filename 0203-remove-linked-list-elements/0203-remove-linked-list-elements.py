# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        all_values = []
        
        while head:
            if head.val != val:
                all_values.append(head.val)
            head = head.next
        
        dummyNode = ListNode()
        new_head = dummyNode

        for value in all_values:
            new_head.next = ListNode(value)
            new_head = new_head.next

        return dummyNode.next