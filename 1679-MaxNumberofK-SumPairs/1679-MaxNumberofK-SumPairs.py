class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        
        num_counts = Counter(nums)
        operations = 0

        for num in nums:
            complement = k - num
            if num_counts[num] > 0 and num_counts[complement] > 0:
                # If num and complement are the same, we need at least two of them
                if num == complement:
                    if num_counts[num] > 1:
                        operations += 1
                        num_counts[num] -= 2
                else:
                    operations += 1
                    num_counts[num] -= 1
                    num_counts[complement] -= 1

        return operations
