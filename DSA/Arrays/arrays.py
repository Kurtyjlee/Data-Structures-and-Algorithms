

# Arrays are defined within square brackets
# python allows you to store different data types in the same array
array = [10.0, 3, "Adam", 5]

# Random indexing into the array O(1)
print(array[0])

# Slicing arrays; 1st position to 3rd
print(array[0:2])

# Last item in the array
print(array[-1])

# Updating a value in an array
array[2] = "Henry"

# Reversing a string
array[::-1]

# Searching an array for the largest number the conventional way O(N)
array1 = [10, 42, 55, 1, 2, 0]
maximum = array[0]
for item in array1:
    if item > maximum:
        maximum = item
print(maximum)

# python style
print(max(array1))
