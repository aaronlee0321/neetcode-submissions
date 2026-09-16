from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_dict = defaultdict(int)
        for num in nums:
            k_dict[num] += 1

        k_dict_ls = []
        for key,value in k_dict.items():
            k_dict_ls.append([value,key])

        sorted_keys = sorted(k_dict_ls,reverse=True)
        sorted_keys = sorted_keys[:k]
        
        
        results = []
        for i in sorted_keys:
            results.append(i[1])
        return results