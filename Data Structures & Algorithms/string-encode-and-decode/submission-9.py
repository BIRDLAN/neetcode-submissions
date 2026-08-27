# Time: O(m), space: O(m + n), m = sum of length of all the strings ,n = number of strings 
class Solution0:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += f"{len(s)}#{s}"
        return encode

    def decode(self, s: str) -> List[str]:
        i = 0 
        decode = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            decode.append(s[i:i + length])
            i += length
        return decode
    








class Solution:
    # Time: O(n), space: O(1), n = numbers of string
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return chr(257)
            

        return chr(256).join(strs)
        

    # Time: O(n), space:O(n), n = length of string 
    def decode(self, s: str) -> List[str]:
        if s == chr(257):
            return []
        strs = s.split(chr(256))
        return strs
            



















            
      