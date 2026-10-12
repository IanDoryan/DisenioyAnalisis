def fibo(n):
    # ENTRADA: n, el término a calcular (n >= 1)
    # SALIDA: el n-ésimo término de la sucesión
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    n = int(input("Término N a calcular: "))
    if n < 1:
        print("N debe ser un entero mayor o igual a 1")
    else:
        print(f"El término {n} es: {fibo(n)}")