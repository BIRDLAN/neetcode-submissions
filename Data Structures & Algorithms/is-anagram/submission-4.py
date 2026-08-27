# Time: O(nlogn + mlogm), space: O(1), n = length of s, m = length of t 
class Solution0:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(sorted_s)):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True
        
# Time: O(n + m), space: O(1), n = length of s, m = length of t 
class Solution1:
   def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for num in s:
            dic[num] += 1
        for num in t:
            if dic[num] - 1 < 0: 
                return False
            dic[num] -= 1
        return True

# Time: O(n + m), space: O(1), n = length of s, m = length of t 
class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    for val in count:
        if val != 0:
            return False
    return True
        