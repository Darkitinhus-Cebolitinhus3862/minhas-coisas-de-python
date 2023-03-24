def tribonacci_array(num, num2):
    if num2 != "":
        n = list(map(int, str(num2)))
    else:
        n = [0, 1 ,1]
    
    nterms = int(num)

    t1, t2, t3 = n[0], n[1], n[2] 
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
        
nu = input("digite os tres numeros iniciais do tribonacci: ")

num = input("digite o numero de termos desejados: ")  

if nu != "":
    print("seram usados", nu,"para o tribonacci com", num, "termos")
else:
    print("seram usados [0, 1, 1] para o tribonacci com", num, "termos")
input()
tribonacci_array(num, nu)

input()
