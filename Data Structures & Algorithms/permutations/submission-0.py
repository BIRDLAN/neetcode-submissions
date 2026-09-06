# Time: O(n * n!),space: O(n), n = length of nums 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(nums: List[int], permute_result: List[int]):
            if len(nums) == 1:
                permute_result.append(nums[0])
                result.append(permute_result)
            for i in range(len(nums)):
                nums[0], nums[i] = nums[i], nums[0]
                permute_result.append(nums[0])
                temp = permute_result[:]
                helper(nums[1:], temp)
                nums[0], nums[i] = nums[i], nums[0]
                permute_result.pop()
        helper(nums, [])
        return result


        