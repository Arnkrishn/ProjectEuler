import time

def collatz_seq_length(num, count=0):
    if num <= 0:
        print "Please provide a non-zero positive input"
        return 0
    elif num == 1:
        return count + 1
    else:
        if num % 2 == 0:
            return collatz_seq_length(num / 2, count + 1)
        else:
            return collatz_seq_length(3 * num + 1, count + 1)


def longest_collatz_seq(limit):
    if limit <= 0:
        print "Please provide a non-zero positive input"
    else:
        max_length = 0
        start_num = 1
        for i in range(1, limit):
            collatz_length = collatz_seq_length(i)
            if collatz_length > max_length:
                max_length = collatz_length
                start_num = i
        print max_length, start_num
        return start_num

#Test
start_time = time.time()
print longest_collatz_seq(1000000)
print time.time() - start_time, " secs"
