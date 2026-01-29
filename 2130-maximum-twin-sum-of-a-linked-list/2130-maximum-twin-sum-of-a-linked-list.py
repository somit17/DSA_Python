# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        my_dict = {}
        if head == None:
            return 0
        length = 0
        while head:
            my_dict[length]=head.val
            head=head.next
            length+=1
        
        max_value = -1
        for i in range(int (length/2)):
            j = length-1-i
            temp = my_dict[i]+my_dict[j]
            if temp > max_value:
                max_value = temp

        return max_value