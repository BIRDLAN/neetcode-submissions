# Time: O(n ^ 2), space: O(n), n = length of nums
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        maximum = 0
        for i in range(len(nums)):
            target = nums[i] + 1
            count = 1
            while target in store:
                target += 1
                count += 1
            maximum = max(count, maximum)
        return maximum
