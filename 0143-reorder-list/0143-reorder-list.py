# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev_node, crnt_node = None, slow

        while crnt_node:
            tmp_next_crnt_node = crnt_node.next
            crnt_node.next = prev_node
            prev_node = crnt_node
            crnt_node = tmp_next_crnt_node

        first, second = head , prev_node
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        return head




        

        