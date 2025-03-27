# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        dummy = ListNode(0)
        start = dummy
        proxy = head
        prev_val = float('inf')
        while proxy:
            if proxy.val == prev_val:
                proxy = proxy.next
                continue
            prev_val = proxy.val
            dummy.next = ListNode(proxy.val)
            dummy = dummy.next
            proxy = proxy.next
        return start.next