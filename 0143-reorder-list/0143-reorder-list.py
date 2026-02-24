# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reversed_list(head):
            current = head
            prev = None
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev

        second = slow.next
        slow.next = None
        second = reversed_list(second)

        first , second_half = head,second
        while second_half: 
            tmp1, tmp2 = first.next, second_half.next
            first.next = second_half
            second_half.next = tmp1
            
            # Move pointers forward
            first, second_half = tmp1, tmp2