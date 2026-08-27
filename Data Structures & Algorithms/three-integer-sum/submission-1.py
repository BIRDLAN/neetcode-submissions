# Time: O(n ^ 2), space: O(n), n = number of input list
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        length = len(nums)
        output = []
        for k in range(length - 2):
            if k - 1 >= 0 and nums[k] == nums[k-1]:
                continue
            i, j = k + 1, length - 1
            target = -nums[k]
            while i < j:
                if i < j and nums[i] + nums[j] == target:
                    output.append([nums[k], nums[i], nums[j]])
                    while i + 1 < j and nums[i] == nums[i+1]:
                        i += 1
                    while j - 1 > i and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                elif i < j and nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -=1
        return output


            



        
        