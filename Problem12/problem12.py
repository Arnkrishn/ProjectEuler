import time

def factor_count(num):
    if num <= 0:
        print "Please provide input greater than 0"
    else:
        count = 1
        for i in range(1, num / 2 + 1):
            if num % i == 0:
                count += 1
        #print num, count
        return count

def gen_triangular_number(factor_limit):
    if factor_limit <= 0:
        print "Please provide input greater than 0"
    else:
        i = 1

        while True:
            triangular_number = i * (i + 1) / 2
            if triangular_number / 2 > factor_limit:
                if factor_count(triangular_number) > factor_limit:
                    return triangular_number
            i += 1

#Test
start_time = time.time()
print gen_triangular_number(500)
print time.time() - start_time, " secs"
