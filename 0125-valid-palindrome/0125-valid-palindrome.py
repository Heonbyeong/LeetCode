import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", s)
        replaced = new_str.replace(" ", "").lower()
        start, end = 0, len(replaced) - 1
        
        if end <= 0:
            return True

        while start < end:
            print(start, end)
            if replaced[start] == replaced[end]:
                start += 1
                end -= 1
            else:
                return False
            
        return True        
    