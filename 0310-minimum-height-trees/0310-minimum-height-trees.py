class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        degree = [0] * n
        # Build graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            degree[a] += 1
            degree[b] += 1

        # Find all leaves
        leaves = []
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        remaining = n
        # Remove leaves layer by layer
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves