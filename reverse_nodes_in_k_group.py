# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = prev = ListNode(0)
        prev.next=head
        count=0
        cur = head
        while cur:
            cur = cur.next
            count +=1
        while count >=k:
            cur = prev.next
            nxt=cur.next
            i=k-1
            while i>0:
                cur.next = nxt.next
                nxt.next=prev.next
                prev.next=nxt
                nxt=cur.next
                i -=1
            prev=cur
            count -=k
        return dummy.next

        