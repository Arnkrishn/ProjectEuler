def factorial(num):
    if num < 0:
        print "Please provide positive input"
    elif num in (0, 1):
        return 1
    else:
        return num * factorial(num - 1)

def lattice_path_count(num):
    if num < 0:
        print "Please provide positive input"
    elif num == 1:
        return 1
    else:
        return factorial(2 * num) / (factorial(2 * num - num) * factorial(num))

#Test
print lattice_path_count(20)
