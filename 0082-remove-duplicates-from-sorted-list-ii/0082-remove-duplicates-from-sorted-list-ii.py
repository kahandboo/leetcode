# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = output = ListNode(0)
        prev.next = head
        curr = head

        while curr:
            nxt = curr.next
            if nxt and curr.val == nxt.val:
                while nxt and curr.val == nxt.val:
                    nxt = nxt.next
                prev.next = nxt
                curr = nxt
            else:
                prev = curr
            curr = nxt


        return output.next