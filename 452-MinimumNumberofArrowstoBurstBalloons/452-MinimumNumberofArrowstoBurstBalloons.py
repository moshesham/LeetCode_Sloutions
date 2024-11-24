class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # Sort the intervals by their end position
        points.sort(key=lambda x: x[1])
        
        # Initialize the number of arrows and the position of the first arrow
        arrows = 1
        current_end = points[0][1]
        
        for start, end in points:
            # If the start of the current balloon is greater than current_end
            # We need a new arrow
            if start > current_end:
                arrows += 1
                current_end = end
        
        return arrows

