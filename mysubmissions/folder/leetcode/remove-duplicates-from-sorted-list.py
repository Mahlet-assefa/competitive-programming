# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev=head
        if not head:
            return None
        while head.next!=None:
            if head.val==head.next.val:
                head.next=head.next.next
                # prev=prev.next
            else:
                head=head.next
        return prev 
        

        