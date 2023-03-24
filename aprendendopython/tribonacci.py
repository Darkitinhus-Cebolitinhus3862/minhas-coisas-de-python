def tribonacci(num):
    nterms = int(num)

    t1, t2, t3 = 0, 1, 1
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
        
n = input("Digite a quantidade de termos para o tribonacci : ")
inte = int(n)
print(tribonacci(inte))

input()