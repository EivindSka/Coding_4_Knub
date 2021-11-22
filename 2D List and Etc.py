

number_grid = [
    [1, 2, 3],  #index 0
    [4, 5, 6],  #index 1
    [7, 8, 9],  #index 2
    [0]
]
number_grid.append("10")
#print(number_grid[3][0])  # index 2 and collum 0 = 7
for row in number_grid:    # Will print every value in number_grid
    for collum in row:
        print(collum)
