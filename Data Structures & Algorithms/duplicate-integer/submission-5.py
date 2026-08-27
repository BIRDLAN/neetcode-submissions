# Time: O(n), space: O(n), n = length of nums 
class Solution0:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for index, num in enumerate(nums):
            value = dic.get(num)
            if value is not None:
                return True
            dic[num] = index
        return False

# Brute Force:
# Time: O(n ^ 2), space: O(1), n = length of nums
class Solution1:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# Sort
# Time: O(nlogn), space: O(1), n = length of nums
class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

# Set
# Time: O(n), space: O(n), n = length of nums
class Solution4:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


# Time: O(n), space: O(n), n = length of nums
class Solution5:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            s.add(num)
        return len(nums) != len(s)
        

#Time: O(n), space: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False






















