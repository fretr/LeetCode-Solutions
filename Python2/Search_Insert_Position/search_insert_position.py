class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # initialize low and high index values
        l = 0
        h = len(nums)-1

        # perform a simple binary search for the target value
        while l < h:
            m = (l+h) / 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m
            else:
                l = m + 1

        # if we can't find the target value, we'll return l as the index where the value should have been
        return l
