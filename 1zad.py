def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[-1]

chislo = input("Введите индекс простого числа: ")
while not chislo.isdigit():  # проверка на целочисленный ввод
    chislo = input(":( ЦЕЛОЕ ПОЛОЖИТЕЛЬНОЕ ЧИСЛО! ")
chislo = int(chislo)
if chislo == 0:
    input("0 Ни туда ни сюда ")
else:
    print(prime(chislo))