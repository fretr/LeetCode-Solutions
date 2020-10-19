class Solution:
    def lengthOfLongestSubstring(self, s):

        # initialize character map
        charMap = {}

        # initialize longestSubstring, and lowIdx
        longestSubstring = 0
        lowIdx = 0

        # iterate through each character in s
        for currentIdx in range(len(s)):
            
            # extract a particular character
            char = s[currentIdx]

            # find the lowest index given the addition of the new character
            lowIdx = max(charMap.get(char, -1), lowIdx)

            # reassign longestSubstring if the new substring is longer
            longestSubstring = max(longestSubstring, currentIdx - lowIdx + 1)

            # add the character as the key, and its index as the value into the character map
            charMap[char] = currentIdx + 1

        return longestSubstring
