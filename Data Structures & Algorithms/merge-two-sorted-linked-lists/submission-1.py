# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Time: O(m + n), space: O(m + n), m = list1, n = list2
class Solution0:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        if list1 == None:
            result = ListNode(list2.val, list2.next)
            return result
        if list2 == None:
            result = ListNode(list1.val, list1.next)
            return result
        
        cur1, cur2, cur_result = list1, list2, result
        while cur1 != None and cur2 != None:
            new_node = ListNode(cur1.val) if cur1.val <= cur2.val else ListNode(cur2.val)
            if cur1.val <= cur2.val:
                cur1 = cur1.next
            else:
                cur2 = cur2.next
            
            if result == None:
                result = new_node
                cur_result = result
            else:
                cur_result.next = new_node
                cur_result = cur_result.next

        while cur1 != None:
            new_node = ListNode(cur1.val)
            cur_result.next = new_node
            cur1 = cur1.next

        while cur2 != None:
            new_node = ListNode(cur2.val)
            cur_result.next = new_node
            cur2 = cur2.next

        return result   


# Time: O(m + n), space: O(1), m = length of list1, n = length of list2
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
        
            cur = cur.next 

        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next

          


