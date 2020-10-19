class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # initialize needle length so we don't have to recompute
        needleLen = len(needle)

        # if the needleLen is 0, return 0 per instructions of task
        if needleLen == 0:
            return 0;

        # initialize index to -1 incase there is no needle in haystack
        index = -1

        # for each start index, check if the characters that follow are the needle
        for startIdx in range(0, len(haystack) - needleLen + 1):

            # if the following characters are the needle, we're done
            if haystack[startIdx:startIdx+needleLen] == needle:
                index = startIdx
                break

        return index
