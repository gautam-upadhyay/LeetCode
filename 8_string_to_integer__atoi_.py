class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0
        
        sign = 1
        i = 0
        
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            sign = 1
            i += 1
        
        while i < len(s) and s[i] == '0':
            i += 1

        nums = 0

        while i < len(s) and s[i].isdigit():
            nums = nums * 10 + int(s[i])
            i += 1
        
        result = nums * sign

        INT_MIN = - pow(2, 31)
        INT_MAX = pow(2, 31) - 1

        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX

        return result