# Sort a one dimensional array of integers containing 0s, 1s and 2s in O(n) 
# without any extra memory- means no extra data structure.

# solution: Find the pivot item. i refers to the first item in the array, k refers
# to the last item and j is the tracker. As j <= k, j is compared to the pivot item,
# to check for the position that it is supposed to be in, for every iteration.
# See below for the solution.

def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

def dutch_flag_problem(array, pivot=1):
    # Trailing from the start
    i = 0
    # Tracking index
    j = 0
    # Trailing from the end
    k = len(array) - 1

    while j <= k:
        # if current int is 0, swaps the value with the start trailer, i.
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
            j += 1
        # if current int is 2, swaps the value with the end trailer, k.
        elif array[j] > pivot:
            swap(array, j, k)
            k -= 1
        # else current int is 1, tracker moves on
        else:
            j += 1

if __name__=="__main__":
    array = [1, 2, 0, 2, 1, 0, 2, 0]
    dutch_flag_problem(array)
    print(array)