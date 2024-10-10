# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_a = []
        list_b = []
        while headA:
            list_a.append(headA)
            headA = headA.next
        while headB:
            list_b.append(headB)
            headB = headB.next

        if list_a and list_b and list_a[-1] == list_b[-1]:
            while list_a and list_b and list_a[-1] == list_b[-1]:
                result = list_a[-1]
                del list_a[-1]
                del list_b[-1]
            return result


        return None