# Time: O(nlogn + mlogm), space: O(1), n = length of s, m = length of t 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(sorted_s)):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True
        
    
        