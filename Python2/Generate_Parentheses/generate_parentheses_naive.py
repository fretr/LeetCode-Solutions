class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # start with two possibilities
        possibilities = ["(", ")"]


        # generate all possibilities
        for i in range(0, 2*n-1):
            open_possibilities = ["(" + s for s in possibilities]
            closed_possibilities = [")" + s for s in possibilities]

            possibilities = open_possibilities + closed_possibilities

        # look through possibilities for correct solution
        solutions = []

        # step through each possibility
        for p in possibilities:

            stack = []

            isValid = True

            # add '(' to stack, pop '(' from stack when ')' is reached
            for c in p:
                if c == "(":
                    stack.append("(")
                else:
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        # if we didn't have anything to pop off the stack, this is not a valid solution
                        isValid = False
                        break

            # if this is a valid solution and the stack is empty, we add it to our solution set
            if isValid and len(stack) == 0:
                solutions.append(p)

        return solutions





        
