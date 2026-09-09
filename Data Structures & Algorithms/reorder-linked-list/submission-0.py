# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Time: O(n), space: O(1), n = length of head 
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(-1, head)
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        cur = slow.next
        slow.next = None
        pre = None 
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next 
        right = pre
        left = head

        while right:
            left_next = left.next
            left.next = right
            left = left_next
            right_next = right.next 
            right.next = left
            right = right_next
            





        #cur = 4
        #nextt = cur.next
        #pre = cur
        #cur.next = pre 
        #cur = next


        
        #[0, 1, 2, 3, 4, 5, 6, 7]
        #[0, 1, 2, 3, 4, 5, 6]
        #0, 1, 2, 3     left_pre: 0, left_next: 1 left: 1           
        #4, 5, 6


        #fast = 0 
        #slow = 3
        #fast = 0, 1, 2, 3 => fast = 0 => fast = 1
        #slow = 7, 6, 5, 4 => slow = 6 => slow = 5 
        
        



            
            
        
        