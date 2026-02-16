from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Step 1: Create graph (adjacency list)
        graph = [[] for _ in range(numCourses)]
        
        # Step 2: Create indegree array
        indegree = [0] * numCourses
        
        # Step 3: Fill graph and indegree
        for a, b in prerequisites:
            graph[b].append(a)   # b → a
            indegree[a] += 1     # a has one more prerequisite
        
        # Step 4: Add courses with 0 indegree to queue
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # Count how many courses we complete
        completed = 0
        
        # Step 5: Process queue
        while queue:
            course = queue.popleft()
            completed += 1
            
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 6: Check if all courses completed
        return completed == numCourses
