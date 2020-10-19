class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestPalindrome = ""
        substringSize = len(s)

        # start with the largest possible substring size, and decrease it until it's equal to 1
        while substringSize > 0:

            startIdx = 0

            # try each starting position possible for a particular substring size
            while startIdx + substringSize <= len(s):

                # initialize the substring
                substring = s[startIdx:startIdx+substringSize]

                # check if the substring is a palindrome, and that it's longer than the current longest palindrome
                if (substring == substring[::-1]) and (len(substring) > len(longestPalindrome)):

                    longestPalindrome = substring

                # increment the starting index for the substring size
                startIdx += 1

            # decrease the substring size
            substringSize -= 1

        return longestPalindrome
