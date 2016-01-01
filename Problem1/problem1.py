def sum_of_products(num1, num2, limit):
    sum = -1
    if num1 <= 0 and num2 <= 0:
        print "Please have at least one of num1 or num2 to be > 0"
        return sum
    elif limit < max(num1, num2):
        print "Please set the limit to be greater than num1 and num2"
        return sum
    else:
        return reduce(lambda x, y: x + y, filter(lambda z: (num1 >= 0 and z % num1 == 0) or (num2 >= 0 and z % num2 == 0), range(1, limit)))

#Test
print sum_of_products(3, 5, 1000)
