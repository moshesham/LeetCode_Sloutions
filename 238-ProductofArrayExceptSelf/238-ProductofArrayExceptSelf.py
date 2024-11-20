class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [1] * length
        
        # Step 1: Calculate prefix products
        prefix = 1
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Calculate suffix products and final result
        suffix = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

