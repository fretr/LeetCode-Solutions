class Solution(object):

    def binary_search(self, nums, target, right=False):

        # initialize low and high indices
        l = 0
        h = len(nums)

        # perform binary search, with special conditions
        while l < h:

            m = (l+h) / 2

            # if we're trying to find the left most target value, we'll increment l until we reach the target value
            # if we're trying to find the right most index, we'll increment l until we've reach h or passed the target value
            if (nums[m] < target) or (nums[m] == target and right):
                l = m + 1
            else:
                h = m

        if right:
            return l-1
        else:
            return l

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:

            return [-1, -1]


        # find the left most index, and right most index
        leftIdx = self.binary_search(nums, target)
        rightIdx = self.binary_search(nums, target, True)

        # if we didn't find any target values (e.g. we've gone through the whole list), return [-1, -1]
        if leftIdx > len(nums) - 1:

            return [-1, -1]

        # if the left most index isn't the target value, return [-1, -1]
        elif nums[leftIdx] != target:

            return [-1, -1]

        # else return the left and right indices we found
        else:

            return [leftIdx, rightIdx]
