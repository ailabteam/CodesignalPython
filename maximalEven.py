def maximalEven(inputArray):

    answer = 0
    for i in range(len(inputArray)):
        if inputArray[i] % 2 == 0 and inputArray[i] > answer:
            answer =  inputArray[i] 
    return answer
