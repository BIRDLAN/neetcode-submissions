class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            value = dic.get(target - num)
            if value is not None:
                return [value, index]
            dic[num] = index
        return []