class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        
        def dfs(path, index, num):
            if index == len(word):
                res.append(path + str(num) if num > 0 else path)
                return
            dfs(path, index + 1, num + 1)
            dfs(path + (str(num) if num > 0 else "") + word[index], index + 1, 0)
            
        dfs("", 0, 0)
        return res