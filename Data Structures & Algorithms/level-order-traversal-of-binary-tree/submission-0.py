# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# Time: O(n), space: O(n), n = length of list
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        dq = deque()
        dq.append(root)
        while len(dq) > 0:
            level_size = len(dq)
            level_list = []
            while level_size > 0:
                front = dq.popleft()
                level_list.append(front.val)
                if front.left:
                    dq.append(front.left)
                if front.right:
                    dq.append(front.right)
                level_size -= 1
            result.append(level_list)
        return result
