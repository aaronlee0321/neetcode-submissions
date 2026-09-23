from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        freq_dict = defaultdict(list)

        for ke,v in count_dict.items():
            freq_dict[v].append(ke)
        
        sorted_ls = dict(sorted(freq_dict.items(), reverse = True, key=lambda item: item[0]))
        print(sorted_ls)
        res = []
        idx = 0
        for key_,v in sorted_ls.items():
            for item in v:
                res.append(item)
                idx += 1
            if idx == k:
                return res

        return res