class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix[0]) - 1
        right_ptr = len(matrix) - 1
        left_ptr = 0

        while left_ptr <= right_ptr:
            mid_ptr = ((right_ptr - left_ptr) // 2) + left_ptr
            print(matrix[mid_ptr][0], matrix[mid_ptr][row_len])
            if matrix[mid_ptr][row_len] >= target and matrix[mid_ptr][0] <= target:
                break
            elif matrix[mid_ptr][0] > target:
                print("here 1" , matrix[mid_ptr][0])
                right_ptr = mid_ptr - 1
            else:
                print("here 2" , matrix[mid_ptr][0])
                left_ptr = mid_ptr + 1

        print("-")

        left = 0
        right = row_len

        while left <= right:
            mid = ((right - left)//2) + left
            print(left,right,mid)
            if matrix[mid_ptr][mid] == target:
                return True
            elif matrix[mid_ptr][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
