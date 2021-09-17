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
        visited = set()
        def dfs(room):
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    dfs(key)                 
        dfs(0)
        return len(visited) == len(rooms)