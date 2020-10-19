class Solution(object):

    def expandAroundCenter(self, s, l, r):
        # helper function which checks if characters match as we go away from the center character
        while(l >= 0 and r < len(s)):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break

        # well return l+1 because we should always end 1 index lower than where we're supposed to
        return l+1, r

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if we don't have any characters to process, then the longest palindrome is ""
        if len(s) == 0:
            return ""

        # we'll initialize the longest palindrome to the first character
        longestPalindrome = s[0]

        # iterate across each possible center c in the string s
        for c in range(0, len(s)):

            # we'll try to expand around the center when there is no center character
            l, r = self.expandAroundCenter(s, c, c)

            # if the palindrome is longer than the current longest, we'll replace it
            if r - l  > len(longestPalindrome):
                longestPalindrome = s[l:r]

            # we'll try to expand around the center when there is a center character
            l, r = self.expandAroundCenter(s, c, c+1)

            # if the palindrome is longer than the current longest, we'll replace it
            if r - l > len(longestPalindrome):
                longestPalindrome = s[l:r]


        return longestPalindrome
