from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_set_sorted = sorted(nums_set)
        n = len(nums_set_sorted)
    
        if n < 1:
            return 0
        print(nums_set_sorted)    
        dict_diff = defaultdict(int)
        for idx in range(n-1):
            dict_diff[idx] = nums_set_sorted[idx + 1] - nums_set_sorted[idx]
        
        dict_diff[n-1] = 0
        max_len = 0
        curr_len = 0
        for k,v in dict_diff.items():
            curr_len += 1
            if v != 1:
                if curr_len > max_len:
                    max_len = curr_len
                curr_len = 0
        
        if max_len == 0:
            max_len = curr_len
        
        return max_len