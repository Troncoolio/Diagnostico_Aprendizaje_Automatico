import random 
import os 
print("***Desafio de la clave olvidada***")
a1 = random.randint(0,9)
a2 = random.randint(0,9)
a3 = random.randint(0,9)
a4 = random.randint(0,9)
a5 = random.randint(0,9)
a6 = random.randint(0,9)
clave = [a1, a2, a3, a4, a5, a6]
clave_sensura = ["*", "*", "*", "*", "*", "*"]
intentos = 0
ganador = False
while True:
    for i in range (len(clave)):
        try :
            digito = int(input("Ingresa el " + str(i + 1) + " digito [0-9]: "))
            if (digito > 9 or digito < 0):
                print("Entrada incorrecta solo valores del 0 al 9")
        except ValueError:
            print("Solo valores numericos 0-9")
            digito = int(input("Ingresa el " + str(i + 1) + " digito [0-9]: "))

        if digito == clave[i]:
            clave_sensura[i] = digito
            print(clave_sensura)
            if ("*" in clave_sensura) == False:
                ganador = True
                break
        else:
            os.system("clear")
            intentos+=1
            break
    print("Personas que lo han intentado: " + str(intentos))
    if ganador:
        print("Usted es millonario apartir de hoy ")

        