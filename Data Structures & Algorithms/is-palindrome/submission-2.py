# Time: O(n), space: O(1), n = length of nums
class Solution0:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1 
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True



def is_alphanumeric(c) -> bool:
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'


# Time: O(n), space: O(1), n = length of s 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not is_alphanumeric(s[left]):
                left += 1
                continue
            if not is_alphanumeric(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            
            




         
            



















    