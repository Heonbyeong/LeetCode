# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            next_queue = deque()
            sum_num = 0
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                sum_num += node.val

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            result.append(sum_num/size)
            queue = next_queue

        return result
    