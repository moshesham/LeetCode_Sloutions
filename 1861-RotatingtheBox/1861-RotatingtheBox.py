class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Step 1: Simulate gravity for each row
        for row in box:
            # Start from the rightmost position
            empty_pos = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    # Reset the empty position when hitting an obstacle
                    empty_pos = j - 1
                elif row[j] == '#':
                    # Move the stone to the rightmost available position
                    row[j], row[empty_pos] = row[empty_pos], row[j]
                    empty_pos -= 1
        
        # Step 2: Rotate the box 90 degrees clockwise
        # Initialize the rotated box with empty cells
        rotated_box = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = box[i][j]
        
        return rotated_box
