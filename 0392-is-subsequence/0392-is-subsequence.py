class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start, end = 0, 0
        cnt = 0
        while start < len(s) and end < len(t):
            if s[start] == t[end]:
                start += 1
                end += 1
                cnt += 1
            else:
                end += 1
        
        return cnt == len(s)