# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Recursive
# Time: O(n), space: O(n), n = length of head
class Solution0:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        tail = head.next
        head.next = None
        new_head = self.reverseList(tail)
        tail.next = head
        return new_head


# Iterative
# Time: O(n), space: O(1), n = length of head
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while (cur.next):
            next_node = cur.next
            cur.next = pre
            pre = cur 
            cur = next_node
        cur.next = pre
        return cur



        
       