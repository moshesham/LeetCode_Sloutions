class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a1=s.split()
        a1=a1[::-1]
        res = ' '.join(a1)
        return res