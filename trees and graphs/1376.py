class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        childs = {}
        for e, m in enumerate(manager):
            if m not in childs:
                childs[m] = [e]
            else:
                childs[m].append(e)
        
        def bfs(emp):
            if emp not in childs:
                return 0
            max_time = 0
            for child in childs[emp]:
                max_time = max(bfs(child), max_time) 
            return max_time + informTime[emp]
        return bfs(headID)