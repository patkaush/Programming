# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1:2 technique.
        #Slow will go one by one
        #Fast will go two steps at a time, this ensures that fast is always ahead double the times of slow. By the time fast reaches end of the List, slow will be at the mid section

        slow = head
        fast = head
        while fast!=None and fast.next != None  :
            slow = slow.next
            fast = fast.next.next
        return slow
