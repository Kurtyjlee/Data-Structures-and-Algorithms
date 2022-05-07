# Design an efficient algorithm to reverse a given integer. 1234 -> 4321

# Solution: While loop to iterate through all the digits. Mod 10 to sieve out the
# last digit and divide by 10 to access the next last digit. Reversed is constructed
# by multiplying by 10 and adding the remainder.

def reverse_int(n):
    reversed = 0

    while n > 0:
        # Sieve out the last digit 1234 -> 4
        remainder = n % 10
        # Removing the last 0 from the number 1230 -> 123. // is the int divider
        n = n // 10
        # Adding the sieved digit into the revered int 4 -> 40 -> 43
        reversed = reversed * 10 + remainder
    
    return reversed

if __name__=="__main__":
    reversed = reverse_int(1234)
    print(reversed)