from opcua import Client
import time
from colorama import Fore
url = 'opc.tcp://localhost:4842/freeopcua/server/'
client = Client(url)

client.connect()
print("Client Connected")

while True:
    TIME = client.get_node("ns=2;i=5")
    timer = TIME.get_value()
    print(Fore.GREEN+f"TIME:{timer}")
    print(Fore.YELLOW+"***************************************")

    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(Fore.BLUE+f"Incoming Temperature Value:{Temperature} K")
    
    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print(Fore.BLUE+f"Incoming Pressure Value:{Pressure} MPa")

    X_OffSet = client.get_node("ns=2;i=4")
    Of_X = X_OffSet.get_value()
    print(Fore.BLUE+f"X Offset Value:{Of_X}nm")

    X_POS = client.get_node("ns=2;i=7")
    Y_POS = client.get_node("ns=2;i=8")
    Z_POS = client.get_node("ns=2;i=9")

    X_Pos = X_POS.get_value()
    Y_Pos = Y_POS.get_value()
    Z_Pos = Z_POS.get_value()

    print(Fore.LIGHTYELLOW_EX+f"X:{X_Pos} Y:{Y_Pos} Z:{Z_Pos}")

    print(Fore.YELLOW+"***************************************\n")
    print(Fore.MAGENTA+"***************************************")

    time.sleep(2)
