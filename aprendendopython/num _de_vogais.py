string = input("Digite uma frase: ")
frase = list(string)
print(frase)
cont = int(0)
vog = "aeiouAEIOU"
for letra in frase:
    if letra in vog: 
        cont = cont + 1
        
print("A frase tem ",cont," vogais")
input()