class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # start with the first number in the list
        idx = 0

        # while we haven't reached the last number in the list
        while idx < len(nums) - 1:

            # if the current number is equal to the next number in the list, delete the current number
            if nums[idx] == nums[idx+1]:
                del nums[idx]

            # otherwise we'll move onto the next number
            else:
                idx += 1

        # return the length of how many numbers are left
        return len(nums)
