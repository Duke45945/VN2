#program 3-1
def row_interchange(input_matrix):
    output_matrix = []
    row_1 = []
    row_2 = []
    row_3 = []
    for i in range(len(input_matrix)):
        row_1.append(input_matrix[i][0])
    for i in range(len(input_matrix)):
        row_2.append(input_matrix[i][1])
    for i in range(len(input_matrix)):
        row_3.append(input_matrix[i][2])
    output_matrix.append(row_1)
    output_matrix.append(row_2)
    output_matrix.append(row_3)

    print(output_matrix)

sample_matrix = [['haa' ,'hii' ,'hoo'], [9, 8, 7], [100, 200, 300]]

row_interchange(sample_matrix)