def swap(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return (num1, num2)

def gcd(num1, num2):
    if num1 <= 0 or num2 <= 0:
        print "Please provide inputs greater than 0"
    else:
        if num2 > num1:
            (num1, num2) = swap(num1, num2)
        while(num2 != 0):
            gcd = num2
            (num1, num2) = swap(num1 % num2, num2)
        return gcd

def lcm(num1, num2):
    if num1 <= 0 or num2 <= 0:
        print "Please provide inputs greater than 0"
    else:
        return (num1 * num2) / gcd(num1, num2)

def smallest_multiple(seq_max, seq_min = 1):
    lcm_seq = seq_min
    for i in range(seq_min, seq_max):
        lcm_seq = lcm(lcm_seq, i + 1)
    return lcm_seq

#Test
print smallest_multiple(10)
print smallest_multiple(20)
