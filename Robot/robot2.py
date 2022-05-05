import rodi
import time

robot = rodi.RoDI()

while True:
    sensor = robot.see()
    if sensor <= 10:
        robot.move_backward() # Movemos el robot hacia atras
        time.sleep(1)
        robot.move_right() # Movemos el robot hacia la derecha
        time.sleep(0.4)
        robot.move_forward() # Movemos el robot hacia adelante
        time.sleep(1)
    else:
        robot.move_forward() # Movemos el robot hacia adelante
        time.sleep(1)
        
    print(sensor)



    #print(robot.see()) # Instanciamos un objeto RoDI
    #time.sleep(0.1) # Leemos el sensor de distancia