try:
    num1 = int(input("Introduz um número inteiro: "))
    num2 = int(input("Introduz outro número inteiro: "))

    if num1 == num2:
        print("Os números são iguais.")
    else:
        print("Os números introduzidos são diferentes.")
        
except ValueError:
    print("Erro: Por favor, introduz apenas números inteiros (positivos ou negativos).")
