from opcua import Server
from random import randint
import datetime
import time
from colorama import Fore

server = Server()

url = 'opc.tcp://localhost:4842/freeopcua/server/'
server.set_endpoint(url=url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)
node = server.get_objects_node()

Param = node.add_object(addspace,"Parameters")


Temp = Param.add_variable(addspace,"Temperature",0)
Press = Param.add_variable(addspace,"Pressure",0)
X_OffSet = Param.add_variable(addspace,"X_Offset",0)
Time = Param.add_variable(addspace,"Time",0)
Temp.set_writable()
Press.set_writable()
Time.set_writable()
X_OffSet.set_writable()

Robot_Poses = node.add_object(addspace,"Robot Poses")
X_Pos = Robot_Poses.add_variable(addspace,"XPos",0)
Y_Pos = Robot_Poses.add_variable(addspace,"YPos",0)
Z_Pos = Robot_Poses.add_variable(addspace,"ZPos",0)

X_Pos.set_writable()
Y_Pos.set_writable()
Z_Pos.set_writable()


server.start()
print("Server started at {}".format(url))


        

while True:
    
    X_OFF = randint(-1,1)
    Temperature = randint(10,50)
    Pressure = randint(200,999)
    TIME = datetime.datetime.now()
    
    X_POS = randint(-10,10)
    Y_POS = randint(-10,10)
    Z_POS = randint(-10,10)


    print(Fore.LIGHTBLUE_EX,X_OFF,Temperature,Pressure,TIME)
    print(Fore.YELLOW+"***************************************")
    print(Fore.LIGHTBLUE_EX,X_POS,Y_POS,Z_POS)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)
    X_OffSet.set_value(X_OFF)

    X_Pos.set_value(X_POS)
    Y_Pos.set_value(Y_POS)
    Z_Pos.set_value(Z_POS)

    time.sleep(2)

"""from asyncua import Client
import asyncio
async def device():
    async with Client(url='opc.tcp://localhost:4843/freeopcua/server/') as client:
        while True:
            # Do something with client
            node = client.get_node('i=85')
            value = await node.read_value()

def main():
    device

if __name__== "__main__":
    main()"""