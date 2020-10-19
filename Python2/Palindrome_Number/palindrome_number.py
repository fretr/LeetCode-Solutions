class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # if x is less than zero or evenly divisible by 10, then it cannot be a palindrome number
        if (x < 0) or (x % 10 == 0) and (x != 0):
            return False
        else:
            # initialize the reversed number
            reversed_number = 0

            # we will continue until the reversed number is greater than x, since at that point we will be left with the first half of x store in reversed_number, and the second half of x left in x
            while x > reversed_number:
                reversed_number *= 10
                reversed_number += x % 10
                x /= 10

        # if the number is evenly lengthed, then each half should be equal
        # if the number is of odd length, then we'll have to divide the middle digit out of the reversed number
        return (reversed_number == x) or (reversed_number / 10 == x)
