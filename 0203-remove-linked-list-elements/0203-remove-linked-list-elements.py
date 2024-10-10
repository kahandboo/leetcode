# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = prev_head = ListNode(0)
        curr = head
        prev.next = curr
        while curr:
            if(curr.val == val):
                prev.next = curr.next
            else:
                prev = curr
            curr = prev.next

        return prev_head.next