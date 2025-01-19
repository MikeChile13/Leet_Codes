# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #initialize length
        length = 1
        proxy = head
        #find the length of the linked list
        while proxy.next:
            proxy = proxy.next
            length +=1
        #if the length is equal to n, remove first node
        if n == length:
            return head.next
        #second proxy is to find the node just before what needs to be cut
        proxy2 = head
        for _ in range(length - n-1):
            proxy2 = proxy2.next
        print(proxy2.val)
        proxy2.next = proxy2.next.next #cutting out the required node.
        return head