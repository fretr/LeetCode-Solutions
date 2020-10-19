class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # strip text from string
        str = str.strip()

        # initialize value to return
        integer = 0

        # set flag to signify whether or not we need to add a negative sign
        is_negative = False

        if len(str) > 0:
            # if the first character is '+', we'll strip it off
            if str[0] == "+":
                str = str[1:]
            # if the first character is '-', we'll strip it off and set
            # the is_negative flag to true
            elif str[0] == "-":
                str = str[1:]
                is_negative = True

        # for each character, we'll add it to the integer or stop processing if we hit a non-numeric character
        for char in str:

            # if the next character is a number, we'll assign the variable to_add
            try:
                to_add = int(char)

            # if it's not, we'll break out of processing the string
            except ValueError:
                break

            # move integer decimal place
            integer *= 10

            # add new number to integer
            integer += to_add


        # make the number negative if it's supposed to be
        if is_negative:
            integer = -integer

        # return the highest 32 bit number if the number is lower
        if integer > 2**31 - 1:
            return 2**31 - 1

        # return the lowest 32 bit number if the number is lower
        elif integer < -2**31:
            return -2**31

        # otherwise, return the integer
        else:

            return integer







        
