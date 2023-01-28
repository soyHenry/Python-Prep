#def factorizar_numero(numero):
#    if (type(numero) != int):
#        return None
#    if (numero < 0):
#        return None
#    factorial = 1
#    for n in range(1, (numero)+1):
#        factorial = factorial * n
#    return factorial

#factorizar_numero()
def factorial(n):
    if (n <1):
        return None
    if n==0 or n==1:
        resultado=1
    elif n>1:
        resultado=n*factorial(n-1)
    return resultado

fact=factorial(5)
print (fact)