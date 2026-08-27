# Time: O(n ^ 2), space: O(n), n = length of nums
class Solution0:
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

# Time: O(nlogn), space: O(n), n = length of nums  
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        sorting = sorted(set(nums))
        i = 1
        maximum, count = 1, 1
    
        while i < len(sorting):
            if sorting[i] - sorting[i - 1] == 1:
                count += 1
            else:
                maximum = max(maximum, count)
                count = 1
            i += 1
        return max(maximum, count)
            
          
