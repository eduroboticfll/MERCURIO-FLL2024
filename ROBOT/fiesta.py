from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

"""
Robot: 
Salida: 
Gadgets: 
"""

def ronda_fiesta(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa):
    
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")

    Frenando_Alonso.use_gyro(True)
    
    print("Lanzando")
    print(f"Frenando settings {Frenando_Alonso.settings()}")
    #Frenando_Alonso.settings(straight_speed=300)
    hub.light.on(Color.GREEN)
    
    Frenando_Alonso.settings(1000,500,500,500)
    motorbrazo_dcha.run_angle(300,120, wait=False)
    Frenando_Alonso.straight(580)
    Frenando_Alonso.turn(-45)
    Frenando_Alonso.straight(185)
    Frenando_Alonso.turn(90)
    Frenando_Alonso.straight(140)
    motorbrazo_dcha.run_angle(300,-120)  #mover motor derecho para colocar detrás de palanca luces
    motorbrazo_izqa.run_angle(800, 320)  #mover motor izquierdo para girar altavoces
    Frenando_Alonso.straight(-80)
    motorbrazo_dcha.run_angle(300, 120) #levanta para evitar volver a bajar luces
    Frenando_Alonso.straight(40)
    
    #motorbrazo_izqa.run_angle(800, -350, wait=False) #gira brazo izquiero para que no golpee al volver
    #motorbrazo_dcha.run_angle(300,100)  #levanta brazo derecho para que no golpee al volver
    #Frenando_Alonso.straight(100) #avanza de nuevo para dejar experto y publico
   
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
    ronda_fiesta(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa)
