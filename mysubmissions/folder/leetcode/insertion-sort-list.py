# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
    
        dummy = ListNode(0)
        curr = head
        prev = dummy
        
        while curr:
            next = curr.next
            while prev.next!= None and prev.next.val < curr.val:
                prev = prev.next
            
            curr.next = prev.next
            prev.next = curr
            prev = dummy
            
            curr = next
        
        return dummy.next