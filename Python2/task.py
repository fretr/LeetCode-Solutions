# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    longestString = 0
    currentString = 0
    expectingB = False

    for letter in S:


        if (not expectingB) and (letter == "A"):
            currentString += 1

        elif (not expectingB) and (letter == "B") and (currentString != 0):
            expectingB = True
            currentString += 1

        elif expectingB and letter == "B":
            currentString += 1

        else:
            if currentString > longestString:
                longestString = currentString

            expectingB = False
            currentString = 0

    return len(S) - longestString



print("BAAABAB - " + str(solution("BAAABAB")) + ", " + str(solution("BAAABAB") == 2))
print("BBABAA " + str(solution("BBABAA")) + ", " + str(solution("BBABAA") == 3))
print("AB" + str(solution("AB")) + ", " + str(solution("AB") == 0))
print("BBBBAAAA" + str(solution("BBBBAAAA")) + ", " + str(solution("BBBBAAAA") == 4))
print("ABAAABBB" + str(solution("ABAAABBB")) + ", " + str(solution("ABAAABBB") == 2))
print("ABABABAB" + str(solution("ABABABAB")) + ", " + str(solution("ABABABAB") == 4))
print("AAAABBBBA" + str(solution("AAAABBBBA")) + ", " + str(solution("AAAABBBBA") == 1))
print("AABBABAAABBB" + str(solution("AABBABAAABBB")) + ", " + str(solution("AABBABAAABBB") == 6))
print("" + str(solution("")) + ", " + str(solution("") == 0))
