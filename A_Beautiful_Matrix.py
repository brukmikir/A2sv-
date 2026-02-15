matrix = []

for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] ==1:
            print(abs(i-j))
            
        
