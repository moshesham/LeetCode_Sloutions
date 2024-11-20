class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # Initialize the base cases
        T0, T1, T2 = 0, 1, 1
        
        # Compute the Tribonacci values iteratively
        for i in range(3, n + 1):
            Tn = T0 + T1 + T2
            T0, T1, T2 = T1, T2, Tn
        
        return T2
