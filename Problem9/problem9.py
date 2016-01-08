import math

def pythagorean_triplet(num):
    if num <= 0:
        print "Please provide an input greater than 0"
    else:
        for i in range(1, num):
            for j in range(1, num):
                if math.sqrt(i * i + j * j) == num - (i + j):
                    print i, j, num - (i + j)
                    return i * j * (num - (i + j))

#Test
print pythagorean_triplet(1000)                        
