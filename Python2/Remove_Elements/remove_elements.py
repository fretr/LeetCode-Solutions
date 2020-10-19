class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # initialize current index
        idx = 0

        # while our current index is less than the length of the nums array ...
        while idx < len(nums):
            # we'll delete the number if it matches our target, and NOT increment idx because the number after will be at the index idx
            if nums[idx] == val:
                del nums[idx]

            # otherwise, we'll increment idx to check the next value
            else:
                idx += 1

        # return the length of the remaining nums array
        return len(nums)
