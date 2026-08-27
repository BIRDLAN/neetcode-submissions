# Time: O(m * nlogn), space: O(m * n), m = number of strings, n = length of the logest string.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            dic[key].append(str)
        return list(dic.values())

        