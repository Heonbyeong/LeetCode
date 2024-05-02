class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # for i in range(n):
        #     index = 0
        #     for j in range(m + n):
        #         if nums2[i] >= nums1[j]:
        #             if j < (m + n) - 1 and nums2[i] < nums1[j+1]:
        #                 index = j

        #     nums1.insert(index, nums2[i])
        #     nums1.pop()  
        #     print(nums1, index)
        merged_dist = nums1[:m] + nums2[:n]
        merged_dist.sort()
        for i in range(m+n):
            nums1[i] = merged_dist[i]