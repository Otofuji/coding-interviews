class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1

        queue = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        order = []

        while queue:
            v = queue.pop(0)
            order.append(v)
            for u in graph[v]:
                inDegree[u] -= 1
                if inDegree[u] == 0:
                    queue.append(u)

        if len(order) < numCourses:
            return []
        return order
