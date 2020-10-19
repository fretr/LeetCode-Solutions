class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral_to_integer = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        total_sum = 0

        idx = 0

        while idx < len(s):

            current_num = numeral_to_integer[s[idx]]

            if idx == len(s) - 1:
                total_sum += current_num
                idx += 1
            elif current_num < numeral_to_integer[s[idx+1]]:
                total_sum += numeral_to_integer[s[idx+1]] -  current_num
                idx += 2
            else:
                total_sum += current_num
                idx += 1


        return total_sum
