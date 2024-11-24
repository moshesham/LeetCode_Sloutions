class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total_sum = 0
        min_abs_val = float('inf')
        neg_count = 0
        
        # Calculate the total sum of absolute values
        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    neg_count += 1
                min_abs_val = min(min_abs_val, abs(val))
        
        # If there are an odd number of negative values,
        # subtract the smallest absolute value twice
        if neg_count % 2 != 0:
            total_sum -= 2 * min_abs_val
        
        return total_sum

