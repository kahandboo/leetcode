# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_val = 0
        l2_val = 0
        n = 1

        while l1 != None:
            l1_val += l1.val * n
            n *= 10 
            l1 = l1.next
        
        n=1

        while l2 != None:
            l2_val += l2.val * n
            n *= 10 
            l2 = l2.next

        result = l1_val + l2_val

        output = head = ListNode(0)
        if result == 0:
            return output
            
        while result > 0:
            head.next = ListNode(result % 10)
            result = result//10
            head = head.next

        head = None

        return output.next