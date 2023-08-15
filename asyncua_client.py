from asyncua import Client
import asyncio
import time
async def Subscriber():
    async with Client(url='opc.tcp://localhost:4842/freeopcua/server/') as client:
        while True:

            node = client.get_node("ns=2;i=2")
            value = await node.read_value()
            print(f"Value:{value}")
            time.sleep(2)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Subscriber())
    loop.close()
if __name__=="__main__":
    main()
