def gregory_leibniz(n):
    suma = 0

    for i in range(n):
        termino = (-1) ** i / (2 * i + 1)
        suma += termino

    return 4 * suma


n = int(input("Ingresa el número de términos: "))

pi_aprox = gregory_leibniz(n)

print("Aproximación de pi:", pi_aprox)
