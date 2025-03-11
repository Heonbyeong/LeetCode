class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        result = 0
        
        for i in range(len(citations)):
            if i < citations[i]:
                result += 1
        
        return result
