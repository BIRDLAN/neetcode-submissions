# Time: O(n), space: O(1), n = len of heights
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(area, res)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res



    

# Time: O(n ** 2), space: O(1), n = length of heights
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                max_area = max(min(heights[i], heights[j]) * (j - i), max_area)
        return max_area
                



#heights = [1, 7, 2, 5, 4, 7, 3, 6]
#
## Brute force 
#case 1
#i = 0, j = 1 => min(h[0], h[1]) * (1 - 0) = 1 => max = 1 
#i = 0, j = 2 => min(h[0], h[2]) * (2 - 0) = 2 => max = 2
#i = 0, j = 3 => min(h[0], h[3]) * (3 - 0) = 3 => max = 3


#case 2 
#i = 0, j = 1 => min(h[0], h[1]) * (1 - 0) = 2 => max = 2
#i = 0, j= 2 => min(h[0], h[2]) * (2 - 0) = 4 => max = 4 
#i = 1, j = 2 => min(h[1], h[2]) * (2 - 1) = 2 => max = 4





















        