class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # simply translate the integer to a string and compare it to its reversed self
        return str(x) == str(x)[::-1]
        
