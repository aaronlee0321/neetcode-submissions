class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_ls = ('{','(','[')
        close_ls = ('}',')',']')
        allowed_pairs = (('(',')'),('[',']'),('{','}'))
        open_stack = []


        for i in range(len(s))        :
            if s[i] in open_ls:
                open_stack.append(s[i])
            else:
                if not open_stack:
                    return False
                elif(open_stack.pop(),s[i]) not in allowed_pairs:
                    return False
        
        if open_stack:
            return False
        return True