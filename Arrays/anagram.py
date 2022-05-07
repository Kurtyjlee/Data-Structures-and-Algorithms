# Construct an algorithm to check whether 2 words are anagrams or not. An anagram is
# formed by rearranging the letters of a different word or phrase

# solution: sort each string and iteratively compare all characters in both strings.

# Overall running time O(n) + O(nlogn) = O(nlogn)
def anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    # Bottleneck O(nlogn) for sorting
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())

    # # object oriented way of solving
    # for item1, item2 in zip(str1, str2):
    #     if item1 != item2:
    #         return False

    # Access array way of solving O(nlogn)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True

if __name__=="__main__":
    str1 = "Hello"
    str2 = "hello"
    anagram(str1, str2)