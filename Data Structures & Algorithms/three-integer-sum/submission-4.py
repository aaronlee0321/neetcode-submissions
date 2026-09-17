class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        i = 0
        j = i + 1
        k = len(nums) - 1

        res = []
        while i < len(nums) - 2 and sorted_nums[i] <= 0:
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                # print(sorted_nums[i] ,sorted_nums[j] ,sorted_nums[k])
                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0:
                    curr_res = [sorted_nums[i] ,sorted_nums[j] ,sorted_nums[k]]
                    res.append(curr_res)
                    j += 1
                    k -= 1
                elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
            while i < len(sorted_nums) - 2 and sorted_nums[i] == sorted_nums[i-1]:
                i += 1

        unique_tuples = set(tuple(triplet) for triplet in res)
        return [list(triplet) for triplet in unique_tuples]
