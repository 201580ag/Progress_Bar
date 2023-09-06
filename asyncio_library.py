import asyncio

async def progress_bar():
    for i in range(10):
        await asyncio.sleep(0.1)
        print(f"Progress: {i + 1}/10")

asyncio.run(progress_bar())