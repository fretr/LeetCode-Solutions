class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        reversed_num = 0
        isNegative = False

        if x < 0:
            x = abs(x)
            isNegative = True

        while x != 0:

            reversed_num *= 10
            reversed_num += (x % 10)
            x /= 10

        if reversed_num > 2**31 - 1:
            return 0
        elif isNegative:
            return -reversed_num
        else:
            return reversed_num
            
