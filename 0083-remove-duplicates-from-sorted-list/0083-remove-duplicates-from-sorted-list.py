# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        all_values = set()
        while head:
            all_values.add(head.val)
            head = head.next


        dummyNode = ListNode()
        tail = dummyNode

        for val in sorted(all_values):
            tail.next = ListNode(val)
            tail = tail.next

        return dummyNode.next