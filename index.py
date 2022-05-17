import time
import multiprocessing
import concurrent.futures

print("CALDULADODA POR MULTIPROCESAMIENTO ")
print(  " El usuario debe ingresar dos numeros por \n"
        " por la consola y el programa realizara el calculo de \n"
        " Suma , Resta, Multiplicacion, y Division ( el segundo numero no puede ser CERO ) ")

numInputCount = 0
number1 = None
number2 = None
errorcount = 0
while( numInputCount < 2 and errorcount < 10 ):
    if(numInputCount == 0):
        print("\nINGRESE EL 1ER NUMERO")
        try:
            number1 = int(input())
            numInputCount += 1
        except:
            number1 = None
            print("Debe digitar un numero valido ")
            errorcount += 1
    elif(numInputCount == 1):
        print("\nINGRESE EL 2do NUMERO")
        error = False
        try:
            number2 = int(input())
            error = number2 == 0
        except:
            error = True
        if(error):
            number2 = None
            print("Debe digitar un numero valido distinto de Cero")
            errorcount += 1
        else:
            numInputCount += 1
print(( " Se agregaron los dos numeros " if(numInputCount >= 2 and errorcount < 10) else " No se agregaron los numeros por error"))

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b

if(numInputCount >= 2 and errorcount < 10):
    print("Numero 1: ", number1, "\nNumero 2: ", number2)
    print("Inicia procesamiento ")

    start  = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor :
        f1 = executor.submit(suma, number1,number2)  
        f2 = executor.submit(resta, number1,number2)
        f3 = executor.submit(multiplicacion, number1,number2)
        f4 = executor.submit(division, number1,number2)
        sum = f1.result()
        res = f2.result()
        mul = f3.result()
        div = f4.result()

        print("resultado: \n    Suma: ", sum,"\n    Resta:",res ,"\n    Multiplicacion: ",mul,"\n   Division:",div)

    finish = time.perf_counter()
    print("Tiempo de Finalizado ", str( finish-start ))
