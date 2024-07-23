# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maximum_level = 0

        if root is None:
            return 0

        while queue:
            level = len(queue)
            
            for i in range(level):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            maximum_level += 1

        return maximum_level