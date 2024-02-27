# basado en el proyecto de https://github.com/coder-ella/lego/blob/main/pybricks/masterpiece/A_main_menu.py

from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.robotics import DriveBase

from diag import run_diagnosticos
from pollo import *
from torre import *
from dragon import *
from lamision_a import *
from lamision_b import *
from fiesta import *
from ruedas import *

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Inicializar los dos motores. Por ejemplo, el motor izquierdo must turn counterclockwise to make the robot go forward.
motor_izqa = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_dcha = Motor(Port.B)
motorbrazo_dcha = Motor (Port.F)
motorbrazo_izqa = Motor (Port.D)

#sensor_dcha = Sensor(Port.C)
#sensor_izqa = Sensor(Port.G)


# Inicializar the drive base. Por ejemplo, el diametro de la rueda es de 62,4mm.
# La distancia entre las dos ruedas es de 103,5mm.
# Nuestro robot es Frenando_Alonso
Frenando_Alonso = DriveBase(motor_izqa, motor_dcha, wheel_diameter=62.4, axle_track=103.5)
default_settings = Frenando_Alonso.settings()

# comienza la programacion del menu selector de misiones

menu_options = ("1", "2", "3","4","5","6", "D", "R") #forward, left, right, back, exit
menu_index = 0
num_options = len(menu_options)

# Clear terminal
print("\x1b[H\x1b[2J", end="")

def do_menu(hub):
    # menu_index is global, so that it can remember what the last menu-index was
    global menu_index
    # Normally, the center button stops the program. But we want to use the
    # center button for our menu. So we can disable the stop button.
    hub.system.set_stop_button(None)
    while True:
        hub.display.char(menu_options[menu_index])
        # Wait for any button.
        pressed = ()
        while not pressed:
            pressed = hub.buttons.pressed()
            wait(10)    
        print(f"pressed: {pressed}")
        # and then wait for the button to be released.
        while hub.buttons.pressed():
            wait(10)

        if Button.BLUETOOTH in pressed:
            # This is the exit key!
            return "X"
  
        # Now check which button was pressed.
        if Button.CENTER in pressed:
            # Center button, this is the selection button, so we can exit the
            # selection loop
            print(f"Selected Index: {menu_index}")
            break
        elif Button.LEFT in pressed:
            # Left button, so decrement menu menu_index.
            menu_index -= 1
            if (menu_index < 0): #roll over!
                menu_index = num_options - 1
        elif Button.RIGHT in pressed:
            # Right button, so increment menu menu_index.
            menu_index += 1
            if (menu_index >= num_options):
                menu_index = 0
        print(f"menu_index:{menu_index}")
    
    # Now we want to use the Center button as the stop button again.
    hub.system.set_stop_button(Button.CENTER)
    selected = menu_options[menu_index]
    print(f"menu option selected {selected}")
    
    return selected

if hub.imu.ready():
    print("IMU is ready")
    hub.display.icon(Icon.HEART)
else:
    print("IMU is NOT ready!")
    hub.speaker.play_notes(["C3/4","D3/4","C2/2"])
    hub.display.icon(Icon.FALSE)


selected = ""
while True:
    try:
        # Based on the selection, choose a program.
        selected = do_menu(hub)
        Frenando_Alonso.settings(default_settings[0],default_settings[1],
        default_settings[2],default_settings[3])
        if selected == "1":
            ronda_pollo(hub, Frenando_Alonso, motor_dcha, motorbrazo_dcha, motorbrazo_izqa)
            menu_index += 1
        elif selected == "2":
            ronda_dragon(hub, Frenando_Alonso, motorbrazo_dcha)
            menu_index += 1
        elif selected == "3":
            ronda_lamision_a(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa)
            menu_index += 1
        elif selected == "4":
            ronda_lamision_b(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa)
            menu_index += 1
        elif selected == "5":
            ronda_torre(hub, Frenando_Alonso, motorbrazo_dcha,motorbrazo_izqa )
            menu_index += 1
        elif selected == "6":
            ronda_fiesta(hub, Frenando_Alonso, motorbrazo_dcha, motorbrazo_izqa)
            menu_index += 1                 
        elif selected == "D":
            print(f"Frenando_Alonso's settings are{Frenando_Alonso.settings()}")
            run_diagnosticos(hub)
        elif selected == "R":
            limpieza(hub, Frenando_Alonso)
        else:
            print(f"don't know selected value {selected}")
            selected = "X"
            # this is the only way to stop PyBricks
            raise SystemExit("Closing program..")
    except SystemExit:
        if selected == "X":
            raise SystemExit()
        Frenando_Alonso.stop()
        motor_izqa.stop()
        motor_dcha.stop()
        hub.speaker.beep(frequency=1, duration = 50)
        while hub.buttons.pressed():
            wait(100) # wait for button to be released

    Frenando_Alonso.stop()
