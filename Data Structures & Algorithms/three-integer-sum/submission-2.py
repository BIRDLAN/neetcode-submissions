# Time: O(n ^ 2), space: O(n), n = number of input list
class Solution0:
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


            






# Time: O(n ** 2), space: O(n), n = length of nums 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Time: O(nlogn), space: O(n)
        copy_nums = nums.copy() 
        s = set()
        for num in nums:   # Time: O(n)
            copy_nums.remove(num)
            left, right, target = 0, len(copy_nums) - 1, -num
            while left < right:  # Time: O(n)
                if copy_nums[left] + copy_nums[right] == target:
                    s.add((num, copy_nums[left], copy_nums[right]))
                    left += 1
                    right -= 1 
                    continue
                elif copy_nums[left] + copy_nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return list(map(list, s))
            






#nums = [-1, 0, 1, 2, -1, -4]
#output = [[-1, -1, 2], [-1, 0, 1]]
#
#case 1: 
#sorted_nums = [-4, -1, -1, 0, 1, 2]
#
#i = 0, sorted_nums[0]: -4, target: 4, new_nums:[-1, -1, 0, 1, 2] -> None, result: None
#i = 1, sorted_nums[1]: -1, target: 1, new_nums: [-1, 0, 1, 2]-> (0, 1), (-1, 2) result: (-1, 0, 1), (-1, -1, 2)
#i = 2, sorted_nums[2]: -1, target: 1, new_nums: [0, 1, 2] -> (0, 1), result: (-1, 0, 1)
#i = 3, sorted_nums[3]: 0, target: 0, new_nums: [1, 2] -> None, target: None
#i = 4, sorted_nums[4]: 1, target: -1, new_nums: [2] -> None
















        