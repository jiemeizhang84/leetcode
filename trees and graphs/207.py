class GNode:
    def __init__(self):
        self.indegree = 0
        self.to_nodes = []

class Solution:    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        graph = collections.defaultdict(GNode)
        total_dep = 0
        
        for pair in prerequisites:
            next_course, prev_course = pair[0], pair[1]
            graph[prev_course].to_nodes.append(next_course)
            graph[next_course].indegree += 1
            total_dep += 1
            
        no_dep_course = collections.deque()
        
        for ind, node in graph.items():
            if node.indegree == 0:
                no_dep_course.append(ind)
                
        remove_dep = 0
        while no_dep_course:
            course = no_dep_course.pop()
            for next_course in graph[course].to_nodes:
                graph[next_course].indegree -= 1
                remove_dep += 1
                
                if graph[next_course].indegree == 0:
                    no_dep_course.append(next_course)
                    
        if remove_dep == total_dep:
            return True
        else:
            return False