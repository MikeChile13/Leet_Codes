# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        back = head
        if back.next is None:
            return back
        while back and back.next:
            if back.val == back.next.val:
                back.next = back.next.next
            else:
                back = back.next
        return head