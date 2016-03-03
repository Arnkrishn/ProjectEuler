def names_score(file_name):
    total_score = 0
    if file_name is None or file_name == '':
        print 'Please provide correct filename'
    else:
        # Read file with names into a list
        for line in open(file_name, 'r').readlines():
            names = line.strip().replace('"', '').split(',')

        names.sort()
        for i in range(len(names)):
            total_score += (i + 1) * (sum(map(ord, list(names[i]))) - len(names[i] * 64))

    return total_score

#Test
print names_score('p022_names.txt')
