class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = (nums1 + nums2)
        merged_list.sort()
        
        dist_size = len(merged_list)
        middle_index = (dist_size // 2)

        if dist_size % 2 == 0: # Even
            return float((merged_list[middle_index - 1] + 
            merged_list[middle_index]) / 2)
        else:
            return float(merged_list[middle_index])