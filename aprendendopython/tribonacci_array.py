def tribonacci_array(num, num2):
    nterms = int(num)

    t1, t2, t3 = num2[0], num2[1], num2[2] 
    count = 0
    #if e elif para n dar nada errado
    if nterms <= 0:
        print("Please enter a positive integer")

    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(t1)
    # gera o tribonacci
    else:
        print("Tribonacci sequence:")
    while count < nterms:
        print(t1)
        nth = t1 + t2 + t3
        # da update nos valores
        t1 = t2
        t2 = t3
        t3 = nth
        count += 1
        
n = input("digite os tres numeros iniciais do tribonacci: ")
if n != "":
    ns = list(map(int, str(n)))
else:
    ns = [0, 1 ,1]
num = input("digite o numero de termos desejados: ")  

print("seram usados", ns,"para o tribonacci com", num, "termos")
input()
tribonacci_array(num, ns)

input()
