def numPalindromo(x):
    original = x
    inv = 0
    arr = []
    while x > 0:
        r = x % 10
        x = x // 10
        arr.append(r)
    n = len(arr)
    for i in range(n):
        inv = inv + arr[i] * 10 ** (n - (i + 1))
    return inv == original

print(numPalindromo(2274))  # False
print(numPalindromo(1221))  # True