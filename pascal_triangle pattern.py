def pascal_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

def print_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(50))

# Change the number of rows as needed
rows = int(input("Enter the number of rows: "))
triangle = pascal_triangle(rows)
print_triangle(triangle)
