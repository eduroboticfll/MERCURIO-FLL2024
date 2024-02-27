from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon       
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def limpieza(hub, Frenando_Alonso):
    # Clear terminal
    print("\x1b[H\x1b[2J", end="")
    default_settings = Frenando_Alonso.settings()
    print(default_settings)
    
    Frenando_Alonso.settings(straight_speed=500, straight_acceleration=500,turn_rate=500, turn_acceleration=500) 
    wait(200)
    Frenando_Alonso.straight(2000)

    Frenando_Alonso.settings(straight_speed=500, straight_acceleration=500,turn_rate=500, turn_acceleration=500) 
    wait(200)
    Frenando_Alonso.straight(-2000)

    Frenando_Alonso.settings(default_settings[0],default_settings[1],default_settings[2],default_settings[3])
    Frenando_Alonso.straight(1000)
        
    hub.speaker.play_notes([
    "G3/4", "G3/4", "G3/4", "C3/4.",  
    "G3/4","F3/4","E3/4","D3/4", "C4/4.",
    "G3/4","F3/4","E3/4","D3/4", "C4/4.",
    "G3/4","F3/4","E3/4","F3/4","D3/4.", 
    ])
    
    print("done")


# this code allows you to run this code directly without using
# the menu system
if __name__ == '__main__':
    hub = InventorHub()
    motor_izqa = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    motor_dcha = Motor(Port.B)
    motorbrazo_dcha = Motor (Port.F)
    motorbrazo_izqa = Motor (Port.D)
    Frenando_Alonso = DriveBase(motor_izqa, motor_dcha, wheel_diameter=62.4, axle_track=103.5)
    limpieza(hub, Frenando_Alonso)
