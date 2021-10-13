class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        hashmap = {
                   "0": "0",
                   "1": "1",
                   "8": "8",
                   "6": "9",
                   "9": "6"
                  }
        result = []
        
        def helper(path, result, start, end):
            if start > end:
                result.append("".join(path))
                return
            
            for num in hashmap:
                if start == end and num in ('6', '9'):
                    continue
                if start != end and start == 0 and num == '0':
                    continue
                path[start], path[end] = num, hashmap[num]
                helper(path, result, start + 1, end - 1)
                
        helper([None] * n, result, 0, n-1)
        return result
