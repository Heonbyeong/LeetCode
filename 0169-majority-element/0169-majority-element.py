class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_nums = set(nums)
        dict_dist = dict.fromkeys(set_nums, 0)

        for i in nums:
            dict_dist[i] += 1

        return max(dict_dist, key = dict_dist.get)