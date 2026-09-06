# Time: O(n * n!),space: O(n ** 2), n = length of nums 
class Solution0:
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


 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visted = [False] * len(nums)
        def back_tracking(path: List[int]):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if visted[i]:
                   continue
                visted[i] = True
                path.append(nums[i])
                back_tracking(path)
                path.pop()
                visted[i] = False
        back_tracking([])
        return result




            
        