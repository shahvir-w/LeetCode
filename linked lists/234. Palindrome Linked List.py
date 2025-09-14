# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # figure out middle of the list
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half of the list
        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        
        # compare two halves of the list
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            
            right = right.next
            left = left.next
        
        return True
