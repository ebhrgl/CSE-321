# QUESTION1
def findMinCost(NY,SF,M):
    size = len(NY)
    # minCostNY is the minimum costs for month n NY
    optN = [0] * size
    # minCostSF is the minimum costs for month n SF
    optS = [0] * size
    # Set first month cost as a min cost for NY and SF
    optN[0] = NY[0]
    optS[0] = SF[0]

    for i in range(1,size):
        optN[i] = NY[i] + min(optN[i - 1], M + optS[i - 1])
        optS[i] = SF[i] + min(optS[i - 1], M + optN[i - 1])

    return min(optN[size-1],optS[size-1])


# QUESTION2
def maxSessions(start, finish ):
   n = len(f)
   count = 1
   print ("Selected activities:")
   # The first activity is always selected
   i = 0
   print (i,end=" ")
   for j in range(n):
      # if start time is greator than or equal to that of previous activity
         if start[j] >= finish[i]:
            print (j,end=" ")
            count = count + 1
            i = j
   print("Session Size", count)


# QUESTION3
def subset_sum(values, sumOfElement):
    subset = {}
    nonZero = positiveNumber(values) + nagativeNumber(values)
    size = len(nonZero)
    # We use this fonk for dynamic programming
    def dynamic(index, subsetsum):

        if subsetsum < sum(nagativeNumber(values)):
            return False
        elif subsetsum > sum(positiveNumber(values)):
            return False
        elif index == 0:
            return nonZero[0] == subsetsum
        # create array for store in dynamic programming
        i = (index, subsetsum)
        if i in subset:
            return subset[i]

        subset[i] = nonZero[index] == subsetsum or dynamic(index-1, subsetsum) or dynamic(index-1, subsetsum-nonZero[index])
        return subset[i]

    return dynamic(size-1, sumOfElement)

def positiveNumber(integers):
    return [integer for integer in integers if integer > 0]

def nagativeNumber(integers):
    return [integer for integer in integers if integer < 0]


# QUESTION4
def minCostAlignment(strA, strB, match,mismatch,gap):
    sizeA = len(strA)
    sizeB = len(strB)
    matrix = [[0 for i in range(sizeB) ] for j in range(sizeA)]
    mincost = 0
    optimmalCell = (0,0)

    for i in range(1, sizeB):
        for j in range(1, sizeA):
            matrix[i][j] = max(matrix[i][j-1] + gap, matrix[i-1][j] + gap,matrix[i-1][j-1] + (match if strA[i] == strB[j] else mismatch), 0)
            # Find largest score cell
            if matrix[i][j] >= mincost:
                mincost = matrix[i][j]
                optimmalCell = (i,j)
                # return the optimal cell and cost
    return mincost, optimmalCell


# QUESTION5
def findMin(arr):
    n = len(arr)
    sum = 0
    i = n - 1
    while (i >= 0):
        if (arr[i] < 0):
            sum -= arr[i]
        else:
            sum += arr[i]
        i -= 1
    print("Sum Of Elements ",sum)

# Driver Code
if __name__ == '__main__':

    print("QUESTION1")
    M = 10
    NY = [1, 3, 20, 30]
    SF = [50, 20, 2, 4]
    print("Moving Cost (M) : ", M)
    print("Total minimum cost: ",findMinCost(NY,SF,M))

    print("QUESTION2")
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    maxSessions(s, f)

    print("QUESTION3")
    values = [10, 3, 9, -5, 4, 2, -7, 8]
    sumOfElement = 0
    if subset_sum(values, sumOfElement=sumOfElement):
        print('The set has a subset sum of ', values)
    else:
        print('The set  does not have a subset sum of ', values)

    print("QUESTION4")
    print("Alignment between minumum cost:")
    print(minCostAlignment("ALIGNME", "SLI  ME", 2, -2, -1))

    print("QUESTION5")
    arr = [-1, -2, -5, 10, 20, 50, 100, 100]
    findMin(arr)






