class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in hashmap:
                val = stack.pop() if stack else ' '
                if val != hashmap[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack