import math
import time

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

def prime_sum(num):
    if num <= 1:
        print "Please enter an input greater than 1"
    else:
        i = 2
        sum = 0
        while i < num:
            if is_prime(i):
                sum += i
            i += 1
        return sum

#Test
start_time = time.time()
print prime_sum(2000000)
print time.time() - start_time, " secs"                
