# Design an algorithm for checking if a given string is a palindrome or not

# Solution: Check if the string is the same as its reversed version

def palindrome_python(s):
    # Checking if the string is equals to the reverse version
    if s == s[::-1]:
        return True
    
    return False

def palindrome(s):
    # Change the string data type into a list data type
    s = list(s)
    original_string = s
    reverse(s)
    reversed_string = s

    # Checks if original and reversed match
    if original_string == reversed_string:
        return True

    return False

# O(N) reverse algorithm previously created
def reverse(array):
    start_index = 0
    end_index = len(array) - 1

    while end_index > start_index:
        # Swap item positions
        array[start_index], array[end_index] = array[end_index], array[start_index]
        start_index += 1
        end_index -= 1

if __name__=="__main__":
    if palindrome('madam'):
        print("Correct")
    else:
        print("Wrong")