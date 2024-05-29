class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            overlap_cnt = nums.count(i)
            while overlap_cnt > 1:
                    nums.remove(i)
                    overlap_cnt -= 1