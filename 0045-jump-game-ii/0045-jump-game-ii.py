class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        max_index = 0
        jump_index = 0

        for i in range(len(nums)-1):
            max_index = max(max_index, i + nums[i])

            if jump_index == i:
                jump_index = max_index
                count += 1
            
        return count
            