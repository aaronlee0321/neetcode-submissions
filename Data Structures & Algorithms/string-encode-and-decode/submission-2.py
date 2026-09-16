class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == None:
            return ""
        
        size_str = ""
        for s in strs:
            size_str += str(len(s)) + ','
        
        new_str = size_str[:-1] + '#'
        for s in strs:
            new_str += s

        print(new_str)
        return new_str

    def decode(self, s: str) -> List[str]:
        mid = list(s).index('#')
        size_str = s[:mid]
        ans_str = s[mid+1:]
        size_ls = size_str.split(',')
        
        results = []
        left = 0
        if size_ls == ['']:
            return []
            
        for i in range(len(size_ls)):
            results.append(ans_str[left:left + int(size_ls[i])])
            left += int(size_ls[i])
        print(results)
        return results
        