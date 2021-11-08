class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(idx, combo):
            if len(digits) == len(combo):
                result.append("".join(combo))
                return
            for letter in hashmap[digits[idx]]:
                combo.append(letter)
                backtrack(idx + 1, combo)
                combo.pop()
                
        result = []
        backtrack(0, [])
        return result