# Time: O(m * nlogn), space: O(m), m = number of strings, n = length of the logest string.
class Solution0:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            dic[key].append(str)
        return list(dic.values())

# Time: O(m * n), space: O(m), m = number of strings, n = length of the logest string.
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for str in strs:
            counts = [0,] * 26
            for i in range(len(str)):
                counts[ord(str[i]) - ord('a')] += 1
            dic[tuple(counts)].append(str)
        return dic.values()


























































# Time: O(m * nlog n), space: O(m), m = number of strings, n = the longest string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            sorted_str = str(sorted(string))
            if dic.get(sorted_str) is None:
                dic[sorted_str] = [string]
            else:
                dic[sorted_str].append(string)
        return list(dic.values())
            
            







        