class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        
        while start < end:            
            sum_number = numbers[start] + numbers[end]
            if sum_number >= target:
                if sum_number == target:
                    break
                end -= 1
            else:
                start += 1   

        return [start+1, end+1]