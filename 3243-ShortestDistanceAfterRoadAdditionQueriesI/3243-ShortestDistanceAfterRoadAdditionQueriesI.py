import heapq

class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Initialize the graph with the initial roads
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append((i + 1, 1))  # road from i to i+1 with weight 1

        def dijkstra(start, end):
            distances = [float('inf')] * n
            distances[start] = 0
            priority_queue = [(0, start)]
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_distance > distances[current_node]:
                    continue
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
            return distances[end]

        result = []
        for u, v in queries:
            graph[u].append((v, 1))  # Add the new road to the graph
            shortest_path = dijkstra(0, n - 1)
            result.append(shortest_path)

        return result

