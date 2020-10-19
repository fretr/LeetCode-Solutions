def solution(N):

    newDigit = 0
    strN = str(N)

    if N == 0:
        return 50

    elif N > 0:
        strN = str(N)
        for idx in range(len(strN)):
            if int(strN[idx]) < 5:
                newDigit = int(strN[0:idx] + "5" + strN[idx:len(strN)])
                break
    else:
        strN = str(abs(N))
        for idx in range(len(strN)):
            if int(strN[idx]) > 5:
                newDigit = -int(strN[0:idx] + "5" + strN[idx:len(strN)])
                break



    return newDigit


    # write your code in Python 3.6



print("268 - " + str(solution(268)) + ", " + str(solution(268) == 5268))
print("670 - " + str(solution(670)) + ", " + str(solution(670) == 6750))
print("0 - " + str(solution(0)) + ", " + str(solution(0) == 50))
print("-999 - " + str(solution(-999)) + ", " + str(solution(-999) == -5999))
