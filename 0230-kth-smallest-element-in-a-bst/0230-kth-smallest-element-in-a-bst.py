# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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
        return val_list[k-1]