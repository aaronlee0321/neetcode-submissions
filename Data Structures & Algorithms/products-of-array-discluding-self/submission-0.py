class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #think of 0 case
        n = len(nums)
        pref = [0] * n
        suff = [0] * n

        pref[0] = 1
        suff[n-1] = 1

        for num in range(1,n):
            pref[num] = nums[num - 1] * pref[num -1]
        

        for i in range(n-2,-1,-1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        res = []
        for j in range(n):
            res.append(pref[j] * suff[j])
        
        return res