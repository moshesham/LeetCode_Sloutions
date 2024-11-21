class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        # Initialize the grid
        grid = [[0] * n for _ in range(m)]
        
        # Mark guards and walls
        for r, c in guards:
            grid[r][c] = 1  # Mark guards with 1
        for r, c in walls:
            grid[r][c] = 2  # Mark walls with 2
        
        # Helper function to mark guarded cells in a direction
        def mark_guarded(r, c, dr, dc):
            while 0 <= r < m and 0 <= c < n:
                if grid[r][c] == 2 or grid[r][c] == 1:
                    break
                if grid[r][c] == 0:
                    grid[r][c] = 3  # Mark guarded cells with 3
                r += dr
                c += dc
        
        # Mark the cells guarded by each guard
        for r, c in guards:
            mark_guarded(r-1, c, -1, 0)  # north
            mark_guarded(r+1, c, 1, 0)   # south
            mark_guarded(r, c-1, 0, -1)  # west
            mark_guarded(r, c+1, 0, 1)   # east
        
        # Count unguarded cells
        unguarded_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded_count += 1
        
        return unguarded_count

