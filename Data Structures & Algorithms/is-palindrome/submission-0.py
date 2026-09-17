import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_list = list(string.ascii_letters + string.digits)
        ls = []
        for c in s:
            if c in alphanumeric_list:
                ls.append(c.lower())
        
        left_ptr = 0
        right_ptr = len(ls) - 1

        while left_ptr < right_ptr:
            if ls[left_ptr] != ls[right_ptr]:
                return False
            left_ptr += 1
            right_ptr -= 1
        
        return True


            