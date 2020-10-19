class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # if there is more than one string, we'll perform vertical scanning
        if len(strs) > 0:

            longest_common_prefix = ""

            # we'll check only for a prefix the length of the smallest word
            for idx in range(0, min(len(s) for s in strs)):

                # we'll grab the character in the first string at the current index
                char = strs[0][idx]

                # compare the character to all other strings (including itself)
                if all(char == s[idx] for s in strs):
                    # if the character matches, it's part of the longest prefix
                    longest_common_prefix += char
                else:
                    # otherwise, we've reached our longest prefix and we can stop processing
                    break;

            return longest_common_prefix

        else:
            return ""
            
