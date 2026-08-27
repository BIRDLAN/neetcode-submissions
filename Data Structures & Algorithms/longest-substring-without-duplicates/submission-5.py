# Time: O(n), space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        max_length, begin = 0, 0
        cur_set = set()
        for end in range(len(s)):
            if s[end] not in cur_set:
                cur_set.add(s[end])
                max_length = max(max_length, len(cur_set))
            else:
                while s[end] in cur_set:
                    cur_set.remove(s[begin])
                    begin += 1
                cur_set.add(s[end])
        return max_length
            
            

        
        
        

        