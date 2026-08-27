# Time: O(n), space: O(n)
class Solution0:
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




















# Time: O(n), space: O(n), n = length of s  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 0
        i, j = 0, 0
        hash_set = set()
        
        while j < len(s):
            hash_set.add(s[j])
            if len(hash_set) != (j - i + 1):
                hash_set.remove(s[i])
                i += 1
                hash_set.add(s[i])
                continue
            max_length = max(max_length, j - i + 1)
            j += 1
        
        return max_length

            
            
        



#s = "zxyzxyz"
#i = 0, j = 0 => s[i] = 'z';, s[j] = 'z' => hash_set: {"z"} => len(hash_set) = 1 == (j - i + 1) => j += 1
#i = 0, j = 1 => s[i] = 'z', s[j] = 'x' => hash_set: {"z", "x"} => len(hash_set) = 2 == (j - i + 1) => j += 1
#i = 0, j = 2 => s[i] = 'z', s[j] = 'y' => hash_set: {"z", "x", "y"} => len(hash_set) = 3 == (j - i + 1) => j += 1
#i = 0, j = 3 => s[i] = 'z', s[j] = 'z' => hash_set: {"z", "x", "y"} => len(hash_set) = 3 < (j - i + 1) => i += 1 => remove h[i] in hash_set: {"x", "y", "z"}
#i = 1, j = 3 => s[i] = 'x', s[j] = 'z'
 
 
 
 


        
        


            
            

        
        
        

        