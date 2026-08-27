#Time: O(n), space: O(m), n = length of s, m = numbers of distinct characters
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        begin = 0
        max_frequency = 0
        dic = {}

        for end in range(len(s)):
            dic[s[end]] = dic.get(s[end], 0) + 1
            max_frequency = max(max_frequency, dic[s[end]])

            if end - begin + 1 > max_frequency + k:
                dic[s[begin]] -= 1
                begin += 1
        return max_frequency + k if len(s) > max_frequency + k else len(s)
            









      
            


            

  


    





            
        
        




      