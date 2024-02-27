from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

"""
Robot: 
Salida: #salimos de la base roja 
#lado derecho en la ultima linea gruesa  
#con el brazo en angulo recto
Gadgets: 
"""

def ronda_dragon(hub, Frenando_Alonso, motorbrazo_dcha):
    
    #Clear terminal
    print("\x1b[H\x1b[2J", end="")

    Frenando_Alonso.use_gyro(True)
    
    print("Lanzando")
    print(f"Frenando settings {Frenando_Alonso.settings()}")
    #Frenando_Alonso.settings(straight_speed=300)
    hub.light.on(Color.GREEN)

    Frenando_Alonso.use_gyro(True)
    Frenando_Alonso.settings(1000,600,800,300)
    motorbrazo_dcha.run_angle (2000,-200, wait=False) #baja brazo
    #sale de la base
    Frenando_Alonso.straight (280)
    Frenando_Alonso.turn (40)
    Frenando_Alonso.straight (207)
    motorbrazo_dcha.run_angle (1000,300) #sube el brazo
    Frenando_Alonso.straight (-15)
    motorbrazo_dcha.run_angle (1000,800) #vuelve a subir el brazo
    #hace mision DJPACO
    Frenando_Alonso.straight (-150) 
    Frenando_Alonso.turn (-40)
    Frenando_Alonso.straight (210) 
    #hace mision DRAGON
    Frenando_Alonso.turn(-90) #gira hacia dragon
    #Frenando_Alonso.straight (20)
    motorbrazo_dcha.run_angle (2000,-400) #baja brazo
    Frenando_Alonso.straight(100) #avanza un poco para meter el brazo en el dragon
    motorbrazo_dcha.run_angle (2000,-400) #baja brazo un poco mas
    Frenando_Alonso.straight (-80) #tira hacia atras
    motorbrazo_dcha.run_angle (2000,1220, wait=False) #sube el brazo para liberar
    Frenando_Alonso.straight(-40)
    Frenando_Alonso.turn(90)
    Frenando_Alonso.straight (215)
    Frenando_Alonso.turn(-45) #gira hacia la mision compartida
    # hace la MISION COMPARTIDA
    Frenando_Alonso.straight (110) 
    #repetir por si equipo contrario no deja en rosa
    Frenando_Alonso.straight (-50)
    Frenando_Alonso.straight (50)
    #
    #   
    #termina la MISION COMPARTIDA y se dirige hacia la ascension
    Frenando_Alonso.straight (-100)
    Frenando_Alonso.turn (135)
    Frenando_Alonso.straight (385) 
    Frenando_Alonso.turn(-90)
    Frenando_Alonso.straight(30)
    motorbrazo_dcha.run_angle (2000,-500) #baja brazo
    Frenando_Alonso.straight(10)
    motorbrazo_dcha.run_angle (2000,-500) #baja brazo
    Frenando_Alonso.straight(10)
    motorbrazo_dcha.run_angle (2000,-500) #baja brazo
    
    motorbrazo_dcha.run_angle (2000, 600) #sube brazo
    Frenando_Alonso.straight(-230)
    Frenando_Alonso.turn(35)
    Frenando_Alonso.straight(-330, Stop.NONE)
    Frenando_Alonso.turn(30, Stop.NONE)
    Frenando_Alonso.straight(-380)

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
    ronda_dragon(hub, Frenando_Alonso, motorbrazo_dcha)
