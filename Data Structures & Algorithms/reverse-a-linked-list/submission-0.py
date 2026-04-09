# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        
        arr = arr[::-1]

        dummy = ListNode(0)
        temp = dummy

        for val in arr:
            temp.next = ListNode(val)
            temp = temp.next

        return dummy.next



        