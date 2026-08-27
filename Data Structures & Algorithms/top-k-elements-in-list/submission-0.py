# Time: O(nlogn), space: O(n), n = length of nums
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        list = []
        for key, value in dic.items():
            list.append((value, key))
        
        list.sort()

        output = []
        
        while len(output) < k:
            output.append(list.pop()[1])
        return output