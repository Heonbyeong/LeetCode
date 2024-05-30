class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            num_count = nums.count(i)
            while num_count > 2:
                nums.remove(i)
                num_count -= 1