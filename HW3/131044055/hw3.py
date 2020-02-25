#QUICK SORT
def partition(array, start, end, count):
    index = start
    high = end
    pivot = array[high]
    for k in range(start, high):
        count += 1
        # If current element is smaller than the pivot
        if array[k] < pivot:
            array[index],array[k] = array[k],array[index]
            index += 1
    array[index],array[high] = array[high],array[index]
    return index, count

# Function to do Quick sort
def quicksort(array, start, end, count):
    if start < end:
        position, count = partition(array, start, end, count)
        count = quicksort(array, start, position - 1, count)
        count = quicksort(array, position + 1, end, count)
    return count


#INSORTION SORT
# Function to do insertion sort
def insertionSort(array):
    # for every element in our array
    count = 0
    for index in range(1, len(array)):
        current = array[index]
        position = index - 1

        while position >= 0 and array[position] > current:
           # print("Swapped {} for {}".format(array[position], array[position-1]))
            array[position+1] = array[position]
          #  print(array)
            position = position - 1
            count += 1
        array[position + 1] = current

    return array,count


import random
def select(n, item):
    pivot = random.choice(item)
    smaller = [item for item in item if item < pivot]
    if len(smaller) > n:
        return select(n, smaller)
    n = n - len(smaller)
    equal = item.count(pivot)
    if equal > n:
        return pivot
    n = n - equal
    bigger = [item for item in item if item > pivot]
    return select(n, bigger)

def findmedian(items):
    n = len(items)
    if n % 2:
        return select(n//2, items)
    else:
        left  = select((n-1) // 2, items)
        right = select((n+1) // 2, items)
        return (left + right) / 2


def subsets(numbers):
    arr = []
    backtrack(arr, [], numbers, 0)
    return arr

def backtrack(res, temp, numbers, start):
    res.append(temp[:])
    size = len(numbers)
    for index in range(start, size):
        temp.append(numbers[index])
        backtrack(res, temp, numbers, index + 1)
        # Backtrack
        temp.pop()

# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
def max(arr,n):

	# Initialize maximum element
	max = arr[0]
	# compare every element with current max
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


# Driver Code
if __name__ == '__main__':
    # Driver code to test above
    x = [19, 12, 1, 8, 15, 22]
    count = quicksort(x, 0, len(x) - 1, 0)
    print(x, "swap size", count)

    array = [19, 12, 1, 8, 15, 22]
    print("Insertionsort: Swap Size:")
    print(insertionSort(array))

    array = [1, 3, 4, 2, 7, 5, 8, 6]
    print("Median =", findmedian(array))

    print(subsets([1, 2, 3]))

    # Driver Code
    array = [10, 324, 45, 90, 9808]
    n = len(array)
    result = max(array, n)
    print("Largest in given array is", result)