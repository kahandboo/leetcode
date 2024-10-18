# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = odd_head = ListNode(0)
        even = even_head = ListNode(0)

        curr = head
        count = 1

        while curr:
            if count % 2 == 0:
                even_head.next = curr
                even_head = even_head.next
            else:
                odd_head.next = curr
                odd_head = odd_head.next
            count += 1
            curr = curr.next

        odd_head.next = even.next
        even_head.next = None

        return odd.next