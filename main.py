def get_tridiagonal_determinant(matrix: list[list[float]]) -> float:
    if not matrix:
        raise ValueError("Matrix is empty")
    
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("Matrix is not square")

    if n == 1:
        return float(matrix[0][0])

    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise ValueError("Matrix is not tridiagonal")

    a = [matrix[i][i] for i in range(n)]
    b = [matrix[i][i + 1] for i in range(n - 1)]
    c = [matrix[i + 1][i] for i in range(n - 1)]

    d_prev2 = 1.0
    d_prev1 = float(a[0])
    current_d = d_prev1

    for i in range(1, n):
        current_d = a[i] * d_prev1 - c[i-1] * b[i-1] * d_prev2
        d_prev2 = d_prev1
        d_prev1 = current_d

    return float(current_d)