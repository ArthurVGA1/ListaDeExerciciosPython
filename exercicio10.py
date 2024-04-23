n = int(input("Digite seu número para ver se é primo ou não primo "))

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "não é um número primo")
            break
    else:
        print(n, "é um número primo")
else:
    print(n, "não é um número primo")