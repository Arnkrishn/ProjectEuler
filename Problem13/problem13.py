def large_sum(input_data_file, num):
    if not input_data_file or num <= 0:
        print "Please provide a non-empty / positive non-zero input"
    else:
        input_data_list = []
        for line in open(input_data_file, 'r').readlines():
            input_data_list.append([int(digit) for digit in line.strip()])

        large_sum = ''
        carry = 0
        input_data_length = len(input_data_list[0])
        for i in range(1, input_data_length + 1):
            sum_str = str(carry + reduce(lambda x, y: x + y, [r[-i] for r in input_data_list]))
            large_sum = sum_str[-1] + large_sum
            carry = int(sum_str[:-1])


        return (str(carry) + large_sum)[:num]


#Test
print large_sum('input_data', 10)
