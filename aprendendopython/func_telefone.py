def create_phone_number(num):
    #formata a lsita em uma string no formato desejado
    phone_number = "({}{}) {}{}{}{}-{}{}{}{}".format(*num)
    return phone_number

n = input("Digite um número de telefone com DDD: ")
#transforma a entrada em uma lista
res = list(map(int, str(n)))
print("The list from number is " + str(res))

input()

phone_number = create_phone_number(res)

print(phone_number)

input()