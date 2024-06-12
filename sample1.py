def print_square(size):
    for i in range(size):
        print('*' * size)
print_square(5)

grid = [[' ' for _ in range(5)] for _ in range(5)]
for i in range(5):
    grid[i][i] = 'X'
    grid[i][4-i] = 'X'
for row in grid:
    print(' '.join(row))

grid = [[' ' for _ in range(5)] for _ in range(5)]
for i in range(5):
    grid[i][0] = '5'
    for j in range(1, i+1):
        grid[i][j] = str(j)
for row in grid:
    print(' '.join(row))




