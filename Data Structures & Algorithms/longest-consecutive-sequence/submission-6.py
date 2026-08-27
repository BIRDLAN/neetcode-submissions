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
class Solution1:
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

# Time: O(n), space: O(n), n = length of nums 
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        output = 0
        for num in store:
            longest = 1
            if num - 1 not in store:
                while num + longest in store:
                    longest += 1
            output = max(output, longest)
        return output




















# Time: O(n), space: O(n), n = length of nums
class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) # Time: O(n)
        longest = 0
        
        for num in s:
            if num - 1 not in s:
                length = 0
                while num + length in s:
                    length += 1
                longest = max(length, longest)
        return longest



# Time: O(nlogn), space: O(n), n = length of nums
class Solution4:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        s = set(nums)
        sorted_set = sorted(s)
        longest = 0
        length = 0
        start = nums[0]
        for num in sorted_set:
            if start + length != num:
                longest = max(length, longest)
                start = num 
                length = 0

            length += 1
        longest = max(length, longest)
        return longest


#Brute force
# Time: O(n ^ 2), space: O(n), n = length of nums
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            count = 0
            while num + count in s:
                count += 1
            longest = max(count, longest)
        return longest
                
                
                
            




            



        
        
        
        
        
        
        
        

         
    ###[2, 20, 4, 10, 3, 4, 5]
    ###{2, 20, 4, 10, 3, 5} -> Time: O(n), space: O(n)
    ###Time: O(n), space: O(n)
    ###2-> 1, 3
    ###20-> 19, 21
    ###4-> 3, 5 
    ###10-> 9, 11
    ###3-> 2, 4, 5, 3
    ### 
    ###
    ###[(2,3,4,5)]
    

    

    
    
    
           

            

                 

            
        



















         

            
          
