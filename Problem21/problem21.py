def sum_of_factors(num):
    if num <= 0:
        print 'Please provide positive non-zero input'
    elif num == 1:
        return 1
    else:
        sum = 0
        for i in range(1, num / 2 + 1):
            if num % i == 0:
                sum += i
    return sum

def amicable_num(num):
    if num <= 1:
        print 'Please provide an input greater than 1'
        return -1
    else:
        amicable_nums = []
        for i in range(1, num + 1):
            i_sum_of_factors = sum_of_factors(i)
            if i_sum_of_factors != i and \
               i == sum_of_factors(i_sum_of_factors) and \
               i_sum_of_factors != 1 and \
               i not in amicable_nums and \
               i_sum_of_factors not in amicable_nums:
                amicable_nums.append(i)
                amicable_nums.append(i_sum_of_factors)

        return sum(amicable_nums)


#Test
print amicable_num(10000)
