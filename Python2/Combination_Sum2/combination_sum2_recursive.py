class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []

        solutions = []

        for idx in range(len(candidates)):

            if candidates[idx] <= target:

                # call recursive function
                self.recursiveSum([candidates[idx]], candidates[idx], candidates[0:idx]+candidates[idx+1:], target, solutions)


        return solutions


    def recursiveSum(self, current_arr, current_sum, candidates, target, solutions):

        if current_sum == target:

            current_arr.sort()

            if current_arr not in solutions:

                solutions.append(current_arr)

        else:

            for idx in range(len(candidates)):

                if current_sum + candidates[idx] <= target:

                    self.recursiveSum(current_arr + [candidates[idx]],
                                      current_sum + candidates[idx],
                                      candidates[0:idx]+candidates[idx+1:],
                                      target,
                                      solutions)

                else:
                    continue

        
