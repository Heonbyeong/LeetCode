# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minimum = 100001
        queue = deque([root])
        val_list = []
        
        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if node.val is not None:
                    val_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        val_list.sort()
        for i in range(len(val_list)-1):
            minus = abs(val_list[i] - val_list[i+1])
            if minimum > minus:
                minimum = minus

        return minimum