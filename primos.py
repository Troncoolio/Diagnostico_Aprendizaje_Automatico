def numeros_primos(inicio, fin):
    primos = []
    for num in range(max(2, inicio), fin):
        es_primo = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos
n = 2
m = 100
print(numeros_primos(n,m))
