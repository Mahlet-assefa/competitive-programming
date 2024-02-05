# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head :
            return True
        if not head.next :
            return True
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        idx_middle = (count - 1) // 2
        idx = 0

        current = head
        next = current.next
        head.next = None
        while next and idx < idx_middle:
            prev = current
            current = next
            next = current.next
            current.next = prev
            idx += 1

        if count % 2 == 0:
            prev = current

       
        while prev and next:
            if prev.val != next.val:
                return False
            
            prev = prev.next
            next = next.next

        return True
