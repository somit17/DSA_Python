# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        prev = dummy_node
        current_head = head
        lookup_set = set(nums)
        while current_head:
            temp = current_head.val
            if temp not in lookup_set:
                prev.next = current_head
                prev = current_head  # CRITICAL: Move prev forward
                current_head = current_head.next
            else:
                current_head = current_head.next

            prev.next = None
            

        return dummy_node.next
        