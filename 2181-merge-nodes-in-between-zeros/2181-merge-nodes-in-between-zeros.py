# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        all_values = []
        
        while head:
            all_values.append(head.val)
            head = head.next
        #print(f"ALL - {all_values}")

        merged_values = []
        count = 0
        for val in all_values:
            count+=val
            if val == 0:
                merged_values.append(count)
                count = 0
        del merged_values[0]
        print(F"{merged_values}")

        dummy_node = ListNode()
        temp_node = dummy_node
        for value in merged_values:
            temp_node.next = ListNode(value)
            temp_node = temp_node.next

        
        return dummy_node.next
                
