class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        in_degrees = [0] * n
        
        # Calculate in-degrees for each node
        for u, v in edges:
            in_degrees[v] += 1
        
        # Find nodes with zero in-degrees
        zero_in_degree_nodes = [i for i in range(n) if in_degrees[i] == 0]
        
        # If there's exactly one node with zero in-degrees, return it
        if len(zero_in_degree_nodes) == 1:
            return zero_in_degree_nodes[0]
        else:
            return -1
