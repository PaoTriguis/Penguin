import rodi
import time

robot = rodi.RoDI() #Instanciamos un objeto RoDI

contador = 0

while  contador != 4:
    robot.move_forward() # Movemos el robot hacia adelante
    time.sleep(1.0)
    robot.move_right() # Movemos el robot hacia la derecha
    time.sleep(0.42)
    contador += 1
robot.move_stop() # Paramos el robot


#robot.move_backward() # Movemos el robot hacia atras
#time.sleep(1.0)
#robot.move_left() # Movemos el robot hacia la izquierda
#time.sleep(1.0)

