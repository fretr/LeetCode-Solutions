class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # initialize solutions and map
        solutions = []

        threeSumMap = {}

        # iterate from 0th index to last
        for i in range(0, len(nums)):

            # starting with the next index
            for j in range(i+1, len(nums)):

                if -nums[j] in threeSumMap:

                    for idx1, idx2 in threeSumMap[-nums[j]]:

                        if j is not idx1 and j is not idx2:

                            solution = sorted([nums[idx1], nums[idx2], nums[j]])

                            if solution not in solutions:

                                solutions.append(solution)

                if nums[i] + nums[j] in threeSumMap:

                    threeSumMap[nums[i] + nums[j]].append((i, j))

                else:

                    threeSumMap[nums[i] + nums[j]] = [(i, j)]

        return solutions
