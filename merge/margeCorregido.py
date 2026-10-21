def merge(A, B, n, m):
    # A y B deben venir ordenados; n = len(A), m = len(B)
    i = 0                 # índice de A
    j = 0                 # índice de B
    k = 0                 # índice de C
    C = [0] * (n + m)     # arreglo nuevo de tamaño n+m

    while i < n and j < m:
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1

    while i < n:          # sobraron elementos de A
        C[k] = A[i]
        i += 1
        k += 1

    while j < m:          # sobraron elementos de B
        C[k] = B[j]
        j += 1
        k += 1

    return C


A = [11, 22, 23, 70]
B = [15, 17, 33, 42, 102]
print(merge(A, B, len(A), len(B)))