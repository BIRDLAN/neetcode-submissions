class Solution0:
    def search(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        if LEN < 1:
            return -1 
        start, end = 0, len(nums) - 1
        
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        
        return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(start: int, end: int)-> int:
            if start > end:
                return -1
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                return helper(start, middle - 1)
            else:
                return helper(middle + 1, end)
        return helper(0, len(nums) - 1)
       
   
