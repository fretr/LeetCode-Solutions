class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # iterate through the list starting with the first index of the vector
        for i in range(0, len(nums)):

            # starting with the next index, we'll iterate through the rest of the vector
            for j in range(i+1, len(nums)):

                # here we'll try every combination to see if its equal to the target value
                if nums[i] + nums[j] == target:


                    # return the indices if there's a match
                    return [i, j]

        #if there's nothing in the list, or nothing sums to the target value we'll raise an exception
        raise RuntimeError("There is supposed to be a solution to twoSum!")
