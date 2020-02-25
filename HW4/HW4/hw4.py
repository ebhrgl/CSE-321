# Question 1.c
def LeftMinRow(a ,col_min ,col_max ,left):
    if ( col_min == col_max ):
        return a[left][col_min]

    row = ( col_min + col_max ) // 2
    index = LeftMinRow(a, col_min, row, left )
    index2 = LeftMinRow(a, row + 1, col_max, left)

    if(index < index2):
        return index
    return index2


#Question 2
def kth(A, B, m, n, k):

    if A == m:
        return B[k]
    elif B == n:
        return A[k]

    midA = int((m - len(A)) / 2)
    midB = int ((n - len(B)) / 2)

    if midA + midB > k:
        if A[midA] > B[midB]:
            return kth(A, B, len(A) + midA, n, k)
        else:
            return kth(A, B, m, len(B) + midB, k)
    else:
        if A[midA] > B[midB]:
            return kth(A, len(B) + midB + 1, m, n, k - midB - 1)
        else:
            return kth(len(A) + midA + 1, B, m, n, k - midA - 1)


# Question 3
# A Divide and Conquer based program for maximum subarray sum problem
def maxSubArraySum(arr, low, high):

    sumleft = 0; sumright = 0; left_sum = 0; right_sum = 0

    if (low == high):
        return arr[high]
        # middle point
    mid = (low + high) // 2

    maxLeftSum = maxSubArraySum(arr, low, mid)
    maxRightSum = maxSubArraySum(arr, mid+1, high)

    for i in range(mid, low - 1, -1):
        sumleft = sumleft + arr[i]
        if (sumleft > left_sum):
            left_sum = sumleft

    for i in range(mid + 1, high + 1):
        sumright = sumright + arr[i]
        if (sumright > right_sum):
            right_sum = sumright

    return max(left_sum + right_sum ,maxRightSum, maxLeftSum)


# Question 4
def checkBipartite(graph):
    queue = []
    color = [-1] * len(graph)

    for i in range(len(l)):
        if  color[i] == -1:
            queue.append(i)
            while queue:
                u = queue.pop(0)

                for v in graph[u]:

                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)

                    elif color[v] == color[u] or v == u:
                        return False

    return True

# Question 5
def maxGain(Cost, Price, left, right):

    diff = Price[right] - Cost[left]

    if right == 0:
        return 0

    elif left == right:
        return diff
    else:
        # Use divide and conquer algorithm
        mid = int((left + right) // 2)
        left_diff = maxGain(Cost, Price, left, mid)
        right_diff = maxGain(Cost, Price, mid + 1, right)

        return max(left_diff, right_diff)

# Driver Code
if __name__ == "__main__":
    # Question 1.c
    print("Question1.c")
    array = [[1, 2, 3], [5, 0, 1], [6, 2, 3]]
    print("row1 min" ,LeftMinRow(array, 0, len(array) - 1, 0))
    print("row2 min", LeftMinRow(array, 0, len(array) - 1, 1))
    print("row3 min", LeftMinRow(array, 0, len(array) - 1, 2))

    # QUESTION 2
    print("Question2")
    A = [3, 8, 11, 13, 9, 7, 27]
    B = [1, 4, 18, 10, 12]
    k = 5
    print(kth(A, B, len(A) + 7, len(B) + 5, k - 1))

    # QUESTION 3
    print("Question3")
    arr = [5, -6, 6, 7, -6, 7, -4, 3]
    n = len(arr)
    max_sum = maxSubArraySum(arr, 0, n - 1)
    print("Maximum contiguous sum is ", max_sum)

    # QUESTION 4
    print("Question4")
    l = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    if checkBipartite(l):
        print("The Graph is Bipartite")
    else:
        print("The Graph is Not Bipartite")

    # QUESTION 5
    print("Question5")
    C = [5, 11, 2, 21, 5, 7, 8, 12, 13]
    P = [7, 9, 5, 21, 7, 13, 10, 14, 20]
    print(maxGain(C, P, 0, len(C) - 1))