from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

"""
Robot: 
Salida: atras del todo, plantilla verde
Gadgets: 
"""

def ronda_lamision_b(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa):
    
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")

    Frenando_Alonso.use_gyro(True)
    
    print("Lanzando")
    print(f"Frenando settings {Frenando_Alonso.settings()}")
    #Frenando_Alonso.settings(straight_speed=300)
    hub.light.on(Color.GREEN)

    Frenando_Alonso.use_gyro(True)
    Frenando_Alonso.settings(1000,500,500,500)
    
    Frenando_Alonso.straight(570)
    Frenando_Alonso.straight(-20)

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
    ronda_lamision_b(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa)
