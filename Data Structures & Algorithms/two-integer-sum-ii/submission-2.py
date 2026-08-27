# Time: O(n), space: O(1), n = length of numbers
class Solution0:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        raise Exception("not found")  
















# Time: O(n), space: O(1), n = length of numbers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
                continue
            else:
                right -= 1
                continue
        raise Exception('no result')





#case 1 
#[1, 2, 3, 4] target = 3 
#left = 1, right = 4 -> 5 > 3 
#left = 1, right = 3 -> 4 > 3
#left = 1, right = 2 -> 3 == 3












        