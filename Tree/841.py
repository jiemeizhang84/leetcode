class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for nb in rooms[node]:
                if not seen[nb]:
                    seen[nb] = True
                    stack.append(nb)
        return all(seen)


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(rooms, visited, roomid):
            if visited[roomid] == True:
                return
            visited[roomid] = True
            for nb in rooms[roomid]:
                dfs(rooms, visited, nb)
         
        visited = [False] * len(rooms) 
        dfs(rooms, visited, 0)
        return all(visited)