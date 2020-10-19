class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:

            return s

        string_rows = [""]*numRows

        up = False
        row_idx = 0

        for idx in range(0,len(s)):

            if up:
                string_rows[row_idx] += s[idx]
                row_idx -= 1
            else:
                string_rows[row_idx] += s[idx]
                row_idx += 1

            if (row_idx == 0) or (row_idx == numRows - 1):
                up = not up


        return "".join(string_rows)
        
