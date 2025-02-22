# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head:Optional[ListNode]) -> Optional[ListNode]:
            prev, temp = None,None

            while head:
                temp = head.next

                head.next = prev

                prev = head
                head = temp
            return prev

        r1 = reverse(l1)
        r2 = reverse(l2)

        total = 0
        rem = 0
        ans = ListNode()

        while r1 or r2:
            if r1:
                total+=r1.val
                r1 = r1.next
            if r2:
                total+=r2.val
                r2 = r2.next

            ans.val = total % 10
            rem = total // 10
            head = ListNode(rem)
            head.next = ans
            ans = head
            total = rem
        
        return ans.next if rem == 0 else ans