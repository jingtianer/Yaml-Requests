import asyncio
import threading
def callBack(k):
    print(str(k) + " is finished")

async def f1(k, callBack):
    await asyncio.sleep(1)
    callBack(k)

async def main():
    result = await asyncio.gather(f1(1, callBack), f1(2, callBack))
    print(result)

def exeTasks():
    threading.Thread(target = lambda :asyncio.run(main())).start()
