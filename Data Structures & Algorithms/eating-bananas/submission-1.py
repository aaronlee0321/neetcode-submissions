import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        left = 1
        right = max(piles)

        while left <= right:
            num_h = ((right - left) // 2) + left
            hr = 0
            for ban in piles: 
                hr += math.ceil(ban/num_h)
            
            if hr <= h:
                k = num_h
                right = num_h - 1
            else:
                left = num_h + 1
        
        return k
