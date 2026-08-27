# Time: O(n), space: O(n), n = length of nums
class Solution0:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            value = dic.get(target - num)
            if value is not None:
                return [value, index]
            dic[num] = index
        return []
# Brute force:
# Time: O(n ^ 2), space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []