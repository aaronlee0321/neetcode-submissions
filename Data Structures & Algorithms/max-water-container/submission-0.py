class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(heights) - 1

        max_vol = 0

        while left_ptr < right_ptr:
            vol = min(heights[left_ptr], heights[right_ptr]) * (right_ptr - left_ptr)
            if vol > max_vol:
                # print(min(heights[left_ptr], heights[left_ptr]) , (right_ptr, left_ptr))
                max_vol = vol

            if heights[left_ptr] > heights[right_ptr]:
                right_ptr -= 1
            else:
                left_ptr += 1
            

        return max_vol