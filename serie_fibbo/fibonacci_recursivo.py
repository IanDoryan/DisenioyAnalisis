def fibo_iterativo(n):
    if n == 1:
        return 0
    a, b = 0, 1          # términos 1 y 2
    for _ in range(n - 2):
        a, b = b, a + b
    return b