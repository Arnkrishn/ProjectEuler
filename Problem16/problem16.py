def power_digit_sum(num):
    if num < 0:
        print "Please provide a positive input"
    else:
        binary_num = int('1'.ljust(num + 1, '0'), 2)
        return reduce(lambda x, y: int(x) + int(y), list(str(binary_num)))

#Test
print power_digit_sum(1000)
