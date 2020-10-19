class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # initialize solutions
        solutions = []

        self.recursiveSub(solutions, candidates, 0, target)

        return solutions


    def recursiveSub(self, solutions, candidates, idx, target, current_sol=list()):

        # if we've reached the target value, append the current result and stop
        if target == 0:
            solutions.append(current_sol)
            return

        # perform a recusive call adding all possible values greater than the current one, but less than the target value
        for i in range(idx ,len(candidates)):
            if candidates[i] <= target:
                # if this is our first recursive call, create a new candidate array with a starting value
                if len(current_sol) == 0:
                    self.recursiveSub(solutions, candidates, i, target-candidates[i], [candidates[i]])

                # otherwise, add the value to the current solution and continue recursing
                else:
                    self.recursiveSub(solutions, candidates, i, target-candidates[i], current_sol+[candidates[i]])

        return

            
