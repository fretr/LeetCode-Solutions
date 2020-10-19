class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x < 0:
            reversed_num = -int(str(abs(x))[::-1])
        else:
            reversed_num = int(str(x)[::-1])

        if (reversed_num > 2**31 - 1) or (reversed_num < -2**31):
            return 0

        return reversed_num
