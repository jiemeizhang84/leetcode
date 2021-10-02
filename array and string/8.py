class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1            
        if ls[0] == '-' or ls[0] == '+':
            del ls[0]
        result = 0
        i = 0
        while i < len(ls) and ls[i].isdigit():
            result = result * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(min(sign * result, 2**31-1), -2**31)