class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        seen_dict = {}

        left_ptr = 0
        seen_dict[s[0]] = 0
        max_len = 1
        curr_len = 1
        for right_ptr in range(1,len(s)):
            if s[right_ptr] in seen_dict.keys():
                if seen_dict[s[right_ptr]] < left_ptr: #its fine
                    curr_len += 1
                else:
                    max_len = max(max_len,curr_len)
                    left_ptr = seen_dict[s[right_ptr]] + 1
                    curr_len = right_ptr - left_ptr + 1
            else:             
                curr_len += 1
            
            seen_dict[s[right_ptr]] = right_ptr
                                
        
        return max(curr_len,max_len)