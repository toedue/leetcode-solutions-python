from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        total = 0

        queue = deque()
        queue.append((root, -1, -1))

        while queue:
            node, parent_val,grandparent_val = queue.popleft()

            if grandparent_val !=-1 and grandparent_val % 2 == 0:
                total += node.val

            if node.left:
                queue.append((node.left, node.val, parent_val))

            if node.right:
                queue.append((node.right, node.val, parent_val))

        return total 
        