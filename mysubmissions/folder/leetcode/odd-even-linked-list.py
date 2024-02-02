# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head:
                odd_tail = head
                cur = head.next
                while cur and cur.next:
                    even_head = odd_tail.next
                    odd_tail.next = cur.next
                    odd_tail = odd_tail.next
                    cur.next = odd_tail.next
                    odd_tail.next = even_head
                    cur = cur.next
            return head