import math

def is_prime(num):
    if num <= 1:
        print "Please enter a number greater than 1"
    elif num in (2, 3):
        return True
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

def largest_prime_factor(num):
    if num <= 1:
        print "Please enter a number greater than 1"
    elif num in (2, 3):
        return num
    else:
        num_sqrt = int(math.sqrt(num))
        for i in range(2, num_sqrt + 1):
            if i == num_sqrt:
                return num
            if num % i == 0:
                return max(i, largest_prime_factor(num / i))


#Test
print largest_prime_factor(3)
print largest_prime_factor(13195)
print largest_prime_factor(600851475143)
