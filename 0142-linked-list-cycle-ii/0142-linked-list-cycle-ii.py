# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        left = head
        right = head
        

        while right and right.next:
            left = left.next
            right = right.next.next
            if left == right:
                break
        else:
            return None

        left = head
        while left != right:
            left = left.next
            right = right.next
            
        return left