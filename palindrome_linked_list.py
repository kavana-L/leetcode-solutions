# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self,head):
        prev = None
        curr = head
        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next=prev
        return curr
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None and head.next is None:
            return True
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        p2=self.reverseLinkedList(slow)
        p1=head
        while p2:
            if p1.val!=p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True
        