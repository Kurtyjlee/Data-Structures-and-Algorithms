# Given a 1 dimensional array of int, construct an algorithm that reverses
# the array in O(N) running time, using constant memory

# Solution: Have an algorithm that swaps the start and end objects
def reverse(array):
    start_index = 0
    end_index = len(array) - 1

    while end_index > start_index:
        # Swap item positions
        array[start_index], array[end_index] = array[end_index], array[start_index]
        start_index += 1
        end_index -= 1

if __name__=="__main__":
    array = [1, 2, 3, 4, 5, 6]
    reverse(array)
    print(array)