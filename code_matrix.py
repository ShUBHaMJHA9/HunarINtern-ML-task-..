def get_matrix():
    order = int(input("Enter the order of the square matrix (e.g., for 3*3, enter 3): "))
    matrix = []
    for i in range(order):
        row = list(map(int, input(f"Enter row {i + 1} values separated by spaces: ").split()))
        matrix.append(row)
    return matrix, order

def sum_diagonal(matrix, order):
    diag_sum = 0
    for i in range(order):
        diag_sum += matrix[i][i]
    return diag_sum

matrix, order = get_matrix()
diagonal_sum = sum_diagonal(matrix, order)
print(f"The sum of the diagonal elements is: {diagonal_sum}")
