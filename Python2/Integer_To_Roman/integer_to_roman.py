class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # initialize place in number (ones, tens, etc.)
        place = 0

        # initialize roman numeral version
        roman_num = ""

        # setup dictionary with values
        numerals = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}


        while num != 0:

            # strip off lowest digit
            value = num % 10

            # divide num by 10 to get to next digit
            num /= 10

            # handle corner cases, using numerals dictionary to access proper digits
            if value == 9:
                roman_num = numerals[10**(place)] + numerals[10**(place+1)]  + roman_num
            elif value > 5:
                roman_num = numerals[(10**(place+1)) / 2] + (value-5)*numerals[(10**(place))] + roman_num
            elif value == 5:
                roman_num = numerals[(10**(place+1)) / 2] + roman_num
            elif value == 4:
                roman_num = numerals[10**(place)] + numerals[(10**(place+1)) / 2] + roman_num
            else:
                roman_num = value*numerals[10**(place)] + roman_num

            # increment which place we're at in the number for accessing characters in dictionary
            place += 1

        return roman_num
