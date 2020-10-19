class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        results = []

        for idx in range(len(nums)):
            self.recursive_permute(nums[:idx]+nums[idx+1:], [nums[idx]], results)

        return results


    def recursive_permute(self, nums, current, results):

        if len(nums) == 0:
            results.append(current)
            return

        for idx in range(len(nums)):
            self.recursive_permute(nums[:idx]+nums[idx+1:], current+[nums[idx]], results)



        
