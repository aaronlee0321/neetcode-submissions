class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right_ptr = len(nums) - 1
        left_ptr = 0

        while left_ptr <= right_ptr:
            mid_ptr = ((right_ptr - left_ptr) // 2) + left_ptr
            print(left_ptr, right_ptr, mid_ptr)
            if nums[mid_ptr] == target:
                return mid_ptr
            elif nums[mid_ptr] > target:
                right_ptr = mid_ptr - 1
            else:
                left_ptr = mid_ptr + 1

        return -1