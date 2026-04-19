import asyncio
import requests

async def func1(k):
    if k ==0 :
        await asyncio.sleep(9)
        print("9")
    elif k ==1 :
        await asyncio.sleep(6)
        print("6")

    else:
        await asyncio.sleep(2)
        print("2")
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open(f"instagram.ico{k}", "wb").write(response.content)
    
    print(f"func{k}")

# async def func2():
#     import requests
#     URL = "https://instagram.com/favicon.ico"
#     response = requests.get(URL)
#     open("instagram2.ico", "wb").write(response.content)
#     # await asyncio.sleep(3)
#     print("func2")

# async def func3():
#     import requests
#     URL = "https://instagram.com/favicon.ico"
#     response = requests.get(URL)
#     open("instagram3.ico", "wb").write(response.content)
#     # await asyncio.sleep(2)
#     print("func3")

async def main():
    
    tasks = [func1(i) for i in range(3)] 
        
    res = await asyncio.gather(*tasks)
    print(res)
asyncio.run(main())
