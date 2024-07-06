# creating a empty list 
matrix = []

# making a nested list 
for i in range(5):
    # Append an empty sublist inside the list
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)

print(matrix)


# Example 2: Filtering a Nested List Using List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        if element%2 == 0:
            row.remove(element)

print(matrix)
