class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        twoSumMap = {}

        # iterate through the list starting with the first index of the vector
        for i in range(0, len(nums)):

            # here we'll see if the difference between the target and the current value exists in the map
            value = twoSumMap.get(target - nums[i])

            if value != None:

                # return the indices if there's a match
                return [value, i]

            # otherwise, we'll add the value, index combo
            twoSumMap[nums[i]] = i

        #if there's nothing in the list, or nothing sums to the target value we'll raise an exception
        raise RuntimeError("There is supposed to be a solution to twoSum!")
