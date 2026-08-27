# Time: O(n), space: O(n), n = length of nums 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for index, num in enumerate(nums):
            value = dic.get(num)
            if value is not None:
                return True
            dic[num] = index
        return False
         