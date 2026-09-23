class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for idx,num in enumerate(nums):
            if num in seen.keys():
               res.append(seen[num])
               res.append(idx)
               return res
            else:
                seen[target-num] = idx        