# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        half = []# store half the values
        slow = head
        fast = head
        while slow and fast:#slow and fast for the middles of the list
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        # print(slow.val)
        # print(half)
        maxv = half[-1]
        n = len(half)-1#using n like this traverses half array in reverse
        while slow:
            maxv = max(maxv,half[n]+slow.val)
            """ instead of adding to the array we  
            can simply get a max of the twin sum at that node"""
            n-=1
            slow = slow.next

        return maxv
