# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_list = []

        curr = head

        while curr:
            my_list.append(curr)
            curr = curr.next

        result = len(my_list)//2

        for _ in range(result):
            head = head.next

        return head
        