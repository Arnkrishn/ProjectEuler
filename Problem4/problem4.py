import math

def is_palindrome(input_str):
    len_str = len(input_str)
    for i in range(0, (len_str / 2) + 1):
        if input_str[i] != input_str[len_str - i - 1]:
            return False
    return True

def largest_palindrome(num_digits):
    if num_digits <= 0:
        print "Please enter a number greater than 0"
    else:
        up_limit = int(math.pow(10, num_digits)) - 1
        low_limit = int(math.pow(10, num_digits - 1))
        low_product_limit = int(math.pow(10, num_digits + 1))
        up_product_limit = int(math.pow(10, num_digits * 2)) - 1

        for i in range(up_product_limit, low_product_limit - 1, -1):
            if is_palindrome(str(i)):
                for j in range(low_limit, up_limit + 1):
                    if i % j == 0 and len(str(i / j)) == num_digits:
                        return i
        print "No palindrome found"

#Test
print largest_palindrome(2)
print largest_palindrome(3)
print largest_palindrome(4)
