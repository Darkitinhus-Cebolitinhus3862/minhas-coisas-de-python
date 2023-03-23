def is_narcissistic(num):
    # transforma o numero em uma string para iterar os digitos
    digits = str(num)
    n = len(digits)
    # calcula a soma das portencias
    sum_of_powers = sum(int(digit) ** n for digit in digits)
    # checa se a soma é igual ao numero original
    return sum_of_powers == num

n = input("Digite um número para checar se ele é narcisista: ")
inte = int(n)
print(is_narcissistic(inte))

input()