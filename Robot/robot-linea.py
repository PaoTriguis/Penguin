import rodi
import time

robot = rodi.RoDI()

while True:
    linea = robot.sense() # Leemos el sensor de distancia
    print((linea[0])) # Imprimimos el sensor de la izquierda
    print(linea[1]) # Imprimimos el sensor de la derecha
    time.sleep(0.5)
    #if linea[0] == 