# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        half = []
        slow = head
        fast = head
        while slow and fast:
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        print(half)
        maxv = half[-1]
        n = len(half)
        while slow:
            maxv = max(maxv,half[n-1]+slow.val)
            n-=1
            slow = slow.next

        return maxv
