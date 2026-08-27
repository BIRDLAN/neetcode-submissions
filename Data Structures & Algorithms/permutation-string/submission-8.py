# Brute force
# Time: O(n * m), space: O(n), n = length of s2, m = length of s1
class Solution0:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1) # Time: O(mlogm)
        for i in range(len(s2) - len(s1) + 1): # Time: O(n - m)
                sorted_sub_s2 = sorted(s2[i:len(s1) + i]) # Time: O(nlogn)
                if sorted_sub_s2 == sorted_s1:
                    return True
        return False
                    
        

# Time: O(n + m), space: O(m), n = length of s2, m = length of s1 
class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_set = [0,] * 26
        s2_set = [0,] * 26
        for n in range(len(s1)):
            s1_set[ord(s1[n]) - ord('a')] += 1
            s2_set[ord(s2[n]) - ord('a')] += 1
        
        i = 0
        for i in range(len(s2) - len(s1) + 1):
            match = 0
            for num in range(26):
                if s1_set[num] == s2_set[num]:
                    match += 1
            if match == 26:
                return True
            if i != len(s2) - len(s1):
                s2_set[ord(s2[i]) - ord('a')] -= 1
                s2_set[ord(s2[i + len(s1)]) - ord('a')] += 1
            
        return False


# Time: O(n), space:O(1), n = length of s2 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        if s2_length < s1_length:
            return False
        
        s1_list = [0,] * 26
        s2_list = [0,] * 26
        
        for num in range(s1_length):
            s1_list[ord(s1[num]) - ord('a')] += 1
            s2_list[ord(s2[num]) - ord('a')] += 1
            
        for i in range(s2_length - s1_length):
            if s1_list == s2_list:
                return True
            s2_list[ord(s2[i]) - ord('a')] -= 1
            s2_list[ord(s2[i + s1_length]) - ord('a')] += 1
        return s1_list == s2_list
            


        
                
            
            

            
       
            











## Time: O(n + m), space: O(m), n = length of s2, m = length of s1 
#s1 = "abc", s2 = "lecabee"
#s1_dict = {"a": 1, "b": 1, "c": 1}
#s2_dict = {"l": 1, "e": 1, "c": 1}
#i = 0
#compare "a" - "z"
#match: 22 != 26 => s2_dict[s2[i]] -= 1, i += 1, s2_dict[s2[i]] += 1 =>
#
#i = 1
# s2_dict = {"e":1, "c": 1, "a":1}
# compare "a" - "z"
# match: 24 != 26 => s2_dict[s2[i]] -= 1, i += 1, s2_dict[s2[i]] += 1 =>
# 
#
#i = 2
#s2_dict = {"c": 1, "a": 1, "b"}
#compare "a" - "z"
#match: 26 => return True
