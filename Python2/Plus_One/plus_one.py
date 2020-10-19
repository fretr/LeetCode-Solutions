class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # if there is no number to process we'll return the number
        if len(digits) == 0:
            return digits

        # add one to the last digit
        digits[-1] += 1

        # initialize index to process from n-1...0
        idx = len(digits) - 1

        # carry a 1 to the next place if necessary
        while digits[idx] == 10 and idx >= 0:

            digits[idx] = 0

            # create a new place if we're at the beginning of the integer
            if idx - 1 == -1:
                digits.insert(0, 1)
            else:
                digits[idx-1] += 1

            # decrement idx
            idx -= 1

        return digits
