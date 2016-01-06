import time
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

def nth_prime(n):
    if n <= 0:
        print "Please provide an input > 0"
    i = 2
    prime_counter = 0
    while True:
        if is_prime(i):
            prime_counter += 1
            if prime_counter == n:
                return i
        i += 1

#Test
start_time = time.time()
print nth_prime(1)
print time.time() - start_time, " secs"
