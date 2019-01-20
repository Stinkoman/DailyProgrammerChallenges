def hasDuplicates(array):
    for elementIndex, element in enumerate(array):
        arrayIndexToCheck = elementIndex + 1
        while arrayIndexToCheck < len(array):
            if element == array[arrayIndexToCheck]:
                return True
            arrayIndexToCheck += 1
    return False

def hasDiagonalThreat(array):
    for arrayPosition, queenValue in enumerate(array):
        arrayLength = len(array)
        indexToCheck = arrayPosition + 1
        while indexToCheck < arrayLength:
            if array[indexToCheck] == ((queenValue-arrayPosition)+indexToCheck) or array[indexToCheck] == ((queenValue+arrayPosition)-indexToCheck):
                return True
            indexToCheck += 1


def queensSolutionIsValid(array):
    if hasDuplicates(array) or hasDiagonalThreat(array):
        return False
    else:
        return True

arrays = [[4, 2, 7, 3, 6, 8, 5, 1],[2, 5, 7, 4, 1, 8, 6, 3],[5, 3, 1, 4, 2, 8, 6, 3],[5, 8, 2, 4, 7, 1, 3, 6],[4, 3, 1, 8, 1, 3, 5, 2]]

for num, array in enumerate(arrays):
    if queensSolutionIsValid(array):
        print("solution " + str(num) + " is valid.")
    else:
        print("solution " + str(num) + " is not valid.")



