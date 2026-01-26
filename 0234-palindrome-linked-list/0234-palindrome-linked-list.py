# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        original = head
        reverse_list = self.reverseLinkedList(self.copyLinkedList(head))
        while original and reverse_list:
            if original.val != reverse_list.val:
                return False
            original = original.next
            reverse_list = reverse_list.next
        return True


    def reverseLinkedList(self,head:Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        last = head
        if head.next:
            last = self.reverseLinkedList(head.next)
            head.next.next=head
        head.next=None
        return last

    def copyLinkedList(self,head:Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = ListNode(head.val)
        new_head.next = self.copyLinkedList(head.next)

        return new_head
        