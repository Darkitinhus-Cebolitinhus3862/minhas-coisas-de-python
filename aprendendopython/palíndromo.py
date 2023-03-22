string = input("Digite uma palavra para saber se é um palíndromo: ")
palavra = list(string)
print(palavra)

reverso = list(reversed(palavra))

print(reverso)

if reverso == palavra:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

input()