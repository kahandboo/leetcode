# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr_for_len = head
        my_list = []
        while curr_for_len:
            my_list.append(curr_for_len.val)
            curr_for_len = curr_for_len.next

        count = len(my_list) - n
        if count == 0 and len(my_list) == 1:
            return None

        curr = head
        prev = None
        
        if count == 0:
            return head.next

        while count > 0:
            prev = curr
            curr = curr.next
            count -= 1
        
        prev.next = curr.next

        return head

        