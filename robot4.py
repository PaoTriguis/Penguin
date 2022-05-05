import rodi
import keyboard 

robot = rodi.RoDI()
robot.move_forward()
while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('w'):  # if key 'q' is pressed 
            robot.move_forward() # Movemos el robot hacia adelante
        elif keyboard.is_pressed('a'):
            robot.move_left() # Movemos el robot hacia la izquierda
        elif keyboard.is_pressed('s'):
            robot.move_backward() # Movemos el robot hacia atras
        elif keyboard.is_pressed('d'):
            robot.move_right() # Movemos el robot hacia la derecha
        elif keyboard.is_pressed('f'):
            robot.move_stop()
    except:
        pass  # if user pressed a key other than the given key the loop will break
