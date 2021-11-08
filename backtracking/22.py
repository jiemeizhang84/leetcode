class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(path, openN, closeN):
            if openN == closeN == n:
                res.append("".join(path))
                return
            if openN < n:
                path.append("(")
                backtrack(path, openN + 1, closeN)
                path.pop()
            if closeN < openN:
                path.append(")")
                backtrack(path, openN, closeN + 1)
                path.pop()
                
        backtrack([], 0, 0)
        return res