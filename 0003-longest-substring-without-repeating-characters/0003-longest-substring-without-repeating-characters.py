class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_dist = set()
        max_len = 0
        count = 0
        max_len = 0

        if len(s) <= 1:
            return len(s)

        for i in range(len(s)):
            for j in range(i, len(s)):
                str_dist.add(s[j])
                count += 1

                if len(str_dist) < count:
                    if max_len < len(str_dist):
                        max_len = len(str_dist)
                    str_dist = set()
                    count = 0
                    break
                    

            

        return max_len