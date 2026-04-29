class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * (numCourses)
        order = []

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1

        queue = deque([])
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # Algorithm - Khan's Alg
        while queue:
            node = queue.popleft()
            order.append(node)

            for neigh in graph[node]:
                in_degree[neigh] -= 1

                if in_degree[neigh] == 0:
                    queue.append(neigh)

        if len(order) != numCourses: # cycle
            return [] 

        return order
