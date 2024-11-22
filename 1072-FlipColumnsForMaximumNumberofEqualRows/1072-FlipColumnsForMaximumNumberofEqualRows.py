class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        def normalize(row):
            """Normalize the row to start with 0."""
            first_val = row[0]
            if first_val == 0:
                return tuple(row)
            else:
                return tuple(1 - x for x in row)

        row_count = defaultdict(int)

        # Normalize each row and count the normalized versions
        for row in matrix:
            normalized_row = normalize(row)
            row_count[normalized_row] += 1

        # The result is the maximum count of any normalized row
        return max(row_count.values())

