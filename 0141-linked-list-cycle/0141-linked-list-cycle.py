# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = head
        turtle = head
        while rabbit is not None and rabbit.next is not None:
            rabbit = rabbit.next.next
            turtle = turtle.next
            
            if rabbit == turtle:  
                return True
        
        return False



        