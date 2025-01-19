# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        proxy = head
        while proxy.next:
            proxy = proxy.next
            length +=1
        if n == length:
            return head.next
        proxy2 = head
        for _ in range(length - n-1):
            proxy2 = proxy2.next
        print(proxy2.val)
        proxy2.next = proxy2.next.next
        return head