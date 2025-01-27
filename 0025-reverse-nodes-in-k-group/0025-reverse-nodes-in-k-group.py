# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:  # Edge case: no reversal needed
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy  # Tail of the previous group
        curr = head   # Current node
        currHead = head  # Start of the current group
        currPrev = None  # Previous node during the reversal process
        count = 0
        
        while curr:
            # Reverse the current link
            temp = curr.next
            curr.next = currPrev
            currPrev = curr
            curr = temp
            
            count += 1  # Increment count for the current group
            
            # If a group of size `k` is formed
            if count == k:
                # Connect the previous group to the current reversed group
                tail.next = currPrev
                # Update tail to the end of the reversed group
                tail = currHead
                # Start a new group
                currHead = curr
                currPrev = None  # Reset prev for the next group
                count = 0  # Reset count for the next group
        
        # Handle the remaining nodes (less than k)
        if count > 0:  # If leftover nodes are not reversed, reverse them back
            curr = currPrev  # Current is at the last node of the partial group
            currPrev = None
            while curr:
                temp = curr.next
                curr.next = currPrev
                currPrev = curr
                curr = temp
            tail.next = currPrev
        else:
            tail.next = curr  # Connect the remaining nodes if exactly divisible by k
        
        return dummy.next
