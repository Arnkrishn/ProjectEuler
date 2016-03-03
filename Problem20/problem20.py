def factorial(num):
    if num <= 0:
        print 'Please provide positive non-zero input'
        return -1
    elif num == 1:
        return 1
    return num * factorial(num - 1)

def factorial_dig_sum(num):
    if num <= 0:
        print 'Please provide positive non-zero input'
        return -1
    else:
        return reduce(lambda x, y: int(x) + int(y), list(str(factorial(num))))

#Test
print factorial_dig_sum(100)
