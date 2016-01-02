import time

def fibo(num):
    return num if num in (1, 2) else fibo(num - 1) + fibo(num - 2)

def even_fibo_sum(val_limit):
    fibo_sum = 0
    i = 1
    if val_limit <= 0:
        print "Please have limit > 0"
    else:
        while 1:
            fibo_num = fibo(i)
            if fibo_num % 2 == 0:
                fibo_sum += fibo_num
            if fibo_num < val_limit:
                i += 1
            else:
                break
    return fibo_sum

#Test
start_time = time.time()
print even_fibo_sum(4000000)
print time.time() - start_time, " seconds"
