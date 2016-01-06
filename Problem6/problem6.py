def sum_square_diff(num):
    if num <= 0:
        print "Please provide the input to be > 0"
    else:
        sum_of_squares = num * (num + 1) * (2 * num + 1) / 6    # sum of squares = n * (n + 1) * (2 * n + 1) / 6
        sum_of_nums = num * (num + 1) / 2                       # sum of first n numbers = n * (n + 1) / 2
        return sum_of_nums * sum_of_nums - sum_of_squares

#Test
print sum_square_diff(10)
print sum_square_diff(100)
