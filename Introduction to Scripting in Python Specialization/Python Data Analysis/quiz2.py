NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)

# print the matrix
#for row in my_matrix:
    #print(row)

n = 0
m = 0

for row in range(0,len(my_matrix)):
    n = n + my_matrix[row][m]
    m = m +1

print(n)

NUM_ROWS = 3
NUM_COLS = 5

# construct a matrix
#my_matrix = {}
#for row in range(NUM_ROWS):
    #row_dict = {}
    #for col in range(NUM_COLS):
        #row_dict[col] = row * col
    #my_matrix[row] = row_dict

#print(my_matrix)

# print the matrix
#for row in range(NUM_ROWS):
    #for col in range(NUM_COLS):
        #print(my_matrix[row][col], end=" ")
    #print()