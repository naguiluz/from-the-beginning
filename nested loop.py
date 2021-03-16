number_grid = [ #this list is made of several other lists. it allows us to create subsets of data within a list, and then access specific pieces inside
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid: #logic flows from the bottom up  #print the value / for each value in a row / for each row in the number grid
    for value in row:
        print(value)