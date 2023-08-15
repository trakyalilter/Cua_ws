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

    print(Fore.YELLOW+"***************************************\n")
    print(Fore.MAGENTA+"***************************************")

    time.sleep(2)
