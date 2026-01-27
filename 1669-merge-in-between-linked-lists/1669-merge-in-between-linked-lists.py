# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummy_node = ListNode(0)
        dummy_node.next = list1
        prev = dummy_node
        start,length=a,0
        current=list1
        while current:
            current=current.next
            length+=1
        #Reset current because we got the length   
        current=list1
        while start > 0:
            current = current.next
            prev=prev.next
            start-=1

        prev.next=None
        while list2:
            prev.next = list2
            list2= list2.next
            prev=prev.next
        
        diff = b-a
        
        while diff > 0:
            current =current.next
            diff-=1

        prev.next=current.next
        return dummy_node.next