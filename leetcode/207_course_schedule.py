class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)

        for course,pre in prerequisites:
            adj_list[pre].append(course)
        
        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1: return False
            if visited[course] == 2: return True

            visited[course] = 1

            for pre in adj_list[course]:
                if not dfs(pre): return False
            
            visited[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
