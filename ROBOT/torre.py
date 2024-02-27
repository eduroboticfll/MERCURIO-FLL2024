from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

"""
Robot: 
Salida: #El robot sale de la BASE ROJA con la rueda derecha en la ultima 
linea gruesa. comienza con los brazos en angulo recto
Gadgets: 
"""

def ronda_torre(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa):
    
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")

    Frenando_Alonso.use_gyro(True)
    
    print("Lanzando")
    print(f"Frenando settings {Frenando_Alonso.settings()}")
    #Frenando_Alonso.settings(straight_speed=300)
    hub.light.on(Color.GREEN)

    Frenando_Alonso.use_gyro(True)
    Frenando_Alonso.settings(1000, 500, 600, 300) #Definimos velocidad y aceleración
    Frenando_Alonso.straight(340)
    Frenando_Alonso.turn(15)
    Frenando_Alonso.straight(400)
    Frenando_Alonso.turn(75)
    Frenando_Alonso.straight(625)
    Frenando_Alonso.settings(turn_acceleration=200, turn_rate=200) #Definimos velocidad y aceleración
    Frenando_Alonso.turn(-90)
    Frenando_Alonso.settings(straight_speed=100, straight_acceleration=100) #cambiamos velocidad para que no vuelque el proyecto
    Frenando_Alonso.straight (100) #va a dejar el proyecto
    Frenando_Alonso.settings(straight_speed=1000, straight_acceleration=500)
    Frenando_Alonso.settings(turn_acceleration=600, turn_rate=300)
    Frenando_Alonso.straight(-90)
    Frenando_Alonso.turn (180)
    Frenando_Alonso.straight(130) #Hacer misión de la torre
    motorbrazo_dcha.run_angle(2000,1400) #sube la peonza
    Frenando_Alonso.straight(-20)
    motorbrazo_dcha.run_angle(2000,400) #sube la peonza
    motorbrazo_dcha.run_angle (2000,-700, wait=False) #baja los brazos
    Frenando_Alonso.straight(-150) #Va para atrás después de hacer la misión
    motorbrazo_dcha.run_angle (2000,800, wait=False) #sube los brazos para no chocar con la flor
    Frenando_Alonso.turn(-90) 
    Frenando_Alonso.straight(80)
    Frenando_Alonso.turn(-25)   #gira hacia la flor
    Frenando_Alonso.settings(turn_acceleration=800, turn_rate=800) 
    Frenando_Alonso.straight(80)
    Frenando_Alonso.turn(20)
    Frenando_Alonso.straight(-20)
    Frenando_Alonso.turn(50)
    Frenando_Alonso.straight(40)
    Frenando_Alonso.turn(-20)
    Frenando_Alonso.settings(straight_acceleration=1000)
    Frenando_Alonso.straight(600)
    Frenando_Alonso.turn(45)
    Frenando_Alonso.straight(450)

    #print("\x1b[H\x1b[2J", end="")
    print("Lunch Complete")

    Frenando_Alonso.use_gyro(False)

if __name__ == '__main__':
    print("Preparado para lanzamiento")
    hub = InventorHub()
    motor_izqa = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    motor_dcha = Motor(Port.B)
    motorbrazo_dcha = Motor (Port.F)
    motorbrazo_izqa = Motor (Port.D)
    Frenando_Alonso = DriveBase(motor_izqa, motor_dcha, wheel_diameter=62.4, axle_track=103.5)
    ronda_torre(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa)
