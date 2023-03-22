tot = 0
for i in range(1, 1000):   
    if i % 3 == 0 or i % 5 == 0:
        tot = tot+i
   
print("A soma de todos os números multiplos de 3 e 5 que estão entre 1 e 1000 é: ",tot)

input()
