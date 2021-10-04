class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(num, target, result, p, val, path, mult):
            if p == len(num):
                if val == target:
                    result.append(path)
                return
            for i in range(p, len(num)):
                if num[p] == '0' and i != p:
                    break
                cur = int(num[p:i+1])
                if p == 0:
                    dfs(num, target, result, i+1, cur, path + str(cur), cur)
                else:
                    dfs(num, target, result, i+1, val+cur, path+"+"+str(cur), cur)
                    dfs(num, target, result, i+1, val-cur, path+"-"+str(cur), -cur)
                    dfs(num, target, result, i+1, val-mult+cur*mult, path+"*"+str(cur), cur*mult)
        result = []
        dfs(num, target, result, 0, 0, '', 0)
        return result