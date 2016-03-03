triangle_list = []

def read_triangle_data(file_name):
    if file_name is None or file_name == '':
        print 'Input file unspecified'
    else:
        triangle_file = open(file_name, 'r')
        for line in triangle_file.readlines():
            triangle_list.append([int(s) for s in line.strip().split(' ')])
        triangle_file.close()


def max_path_triangle(file_name):
    read_triangle_data(input_file)

    triangle_height = len(triangle_list)
    working_list_1 = [triangle_list[0][0]]
    working_list_2 = []

    for i in range(1, triangle_height):
        row_len = len(triangle_list[i])
        for j in range(row_len):
            if j == 0:
                working_list_2.append(triangle_list[i][j] + working_list_1[j])
            elif j == row_len - 1:
                working_list_2.append(triangle_list[i][j] + working_list_1[j - 1])
            else:
                working_list_2.append(max(triangle_list[i][j] + working_list_1[j - 1], triangle_list[i][j] + working_list_1[j]))
        working_list_1 = working_list_2
        working_list_2 = []

    return max(working_list_1)


#Test
input_file = 'p067_triangle.txt'
print max_path_triangle(input_file)
#print triangle_list
