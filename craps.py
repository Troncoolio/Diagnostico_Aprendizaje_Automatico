import time, random
ganador = False
dado_1 = 0
dado_2 = 0
tiro = 0
punto = 0
while not ganador:
    print("Lanzar dados...")
    time.sleep(3)
    dado_1 = random.randint(1,6)
    time.sleep(1)

    print("Dado 1: " + str(dado_1) )
    dado_2 = random.randint(1,6)
    time.sleep(1)

    print("Dado 2: " + str(dado_2) )
    time.sleep(.500)

    tiro += 1
    suma = dado_1 + dado_2
    print("Suma: " + str(suma))
    if tiro == 1:
        match suma:
            case 7, 11:
                ganador = True
                print("USTED GANA")
            case 2, 3, 12:
                print("GAME OVER")
                break
            case 4, 5, 6, 8, 9, 10:
                punto = suma
                
    else :
        match suma:
            case 7: 
                print("GAME OVER")
                break
            case punto:
                print("USTED GANA")
                ganador = True
            
