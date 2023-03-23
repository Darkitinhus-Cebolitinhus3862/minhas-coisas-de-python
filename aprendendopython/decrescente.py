def decrescente(num):
   dec_feito = sorted(num, reverse=True)
   return dec_feito

n = input("digite numeros: ")
ns = list(map(int, str(n)))
print(ns)
input()
dec = decrescente(ns)
print(dec)
input()