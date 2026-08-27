#Time: O(n), space: O(m), n = length of s, m = numbers of distinct characters
class Solution0:
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
            






# Brute force Time: O(n ** 3), space: O(n), n = length of s
# Time: O(n ** 3), space: O(n), n = length of s
class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 1
        for i in range(len(s)):
            count_dic = defaultdict(int)
            for j in range(i, len(s)):
                count_dic[s[j]] += 1
                most_frequency = 1
                for value in count_dic.values():
                    most_frequency = max(most_frequency, value)
                if j - i + 1 - most_frequency <= k:
                    max_length = max(max_length, j - i + 1)
        return max_length
                


#"XYYX", k = 2
#question:
#1. 哪時候要換?
#2. 誰要被換?
#3. 換成誰?
#
#
## Brute force Time: O(n ** 3), space: O(n), n = length of s 
#1. 找出所有 substrings => i = 0 ~ n - 1, j = i + 1 ~ n => O(n ** 2)
#2. 檢查每個 substring 透過最多替換 k 次是否能達到整個 substring with one character => len(substring) - the most frequency character < K => O(n)
#3. if 可以 the max_length = max(max_length, len(substring))
#



# Time: O(), space: O(), n = 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        max_length, most_frequency = 0, 0
        dic = defaultdict(int)
        while j < len(s):
            dic[s[j]] += 1
            most_frequency = max(most_frequency, dic[s[j]])
            if j - i + 1 - most_frequency <= k:
                max_length = max(max_length, j - i + 1)
                j += 1
                continue
            dic[s[i]] -= 1
            dic[s[j]] -= 1
            i += 1
        return max_length


            
            
            

    

#s = "XYYX", k = 2 
#hash_set = {}, max_length = 0, most_frequency = 0, 
#
#i = 0, j = 0 => s[i] = X, s[j] = X => hash_set["X"] => most_frequency = 1 => (j - i - 1) - most_frequency < k 
#i = 0, j = 1 => s[i] = Y, s[j] = Y => hash_set["X", "Y"] => most_frequency = 1 => (j - i - 1) - most_frequency < k 
#i = 0, j = 1 => s[i] =
#
#s = "AAABABB", k = 2
#hash_set = {}, max_length = 0, most_frequnecy = 0
#
#i = 
#







      
            


            

  


    





            
        
        




      