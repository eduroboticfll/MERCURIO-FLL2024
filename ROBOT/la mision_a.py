from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

"""
Robot: 
Salida: #RONDA CAMARA Y BARCO #El robot sale de la base roja, atras del todo, 
plantilla verde
Gadgets: 
"""

def ronda_lamision_a(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa):
    
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")

    Frenando_Alonso.use_gyro(True)
    
    print("Lanzando")
    print(f"Frenando settings {Frenando_Alonso.settings()}")
    hub.light.on(Color.GREEN)

    Frenando_Alonso.use_gyro(True)
    Frenando_Alonso.settings(1000, 500, 1000, 500) #Definimos velocidad y aceleración
    motorbrazo_dcha.run_angle(200,50, wait=False) #levanta brazo
    watch = StopWatch()
    while not motorbrazo_dcha.done() and not motorbrazo_dcha.stalled()  and not watch.time() > 2000:
        wait(10)
    Frenando_Alonso.straight(540)
    motorbrazo_dcha.run_angle(300,-240, wait=False) #baja brazo para coger camara
    #esperamos hasta que bloquee el brazo derecho o complete la accion
    watch = StopWatch()
    while not motorbrazo_dcha.done() and not motorbrazo_dcha.stalled() and not watch.time() > 2000:
        wait(10)
    motorbrazo_dcha.run_angle(200, 40)
    Frenando_Alonso.turn(-10)
    Frenando_Alonso.straight(-150) #atras
    Frenando_Alonso.turn(-50) #gira para dejar camara
    motorbrazo_dcha.run_angle(400,180) #levanta brazo
    ''' eliminamos mientras no tengamos tiempo suficiente
    Frenando_Alonso.turn(-40) #gira para no golpear camara
    Frenando_Alonso.straight(230)
    Frenando_Alonso.turn(-80)
    Frenando_Alonso.settings(1000, 1000, 600, 250)
    Frenando_Alonso.straight(-1500)
    motorbrazo_izqa.run_angle(2000,230)
    '''
    #volvemos a base directamente
    Frenando_Alonso.turn(50)
    Frenando_Alonso.straight(-300)

    #print("\x1b[H\x1b[2J", end="")
    print("Completado")

    Frenando_Alonso.use_gyro(False)

if __name__ == '__main__':
    print("Preparado para lanzamiento")
    hub = InventorHub()
    motor_izqa = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    motor_dcha = Motor(Port.B)
    motorbrazo_dcha = Motor (Port.F)
    motorbrazo_izqa = Motor (Port.D)
    Frenando_Alonso = DriveBase(motor_izqa, motor_dcha, wheel_diameter=62.4, axle_track=103.5)
    ronda_lamision_a(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa)
