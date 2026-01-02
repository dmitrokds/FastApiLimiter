import aiohttp
import time

async def req(sess, num):
    async with sess.post(
        "http://127.0.0.1:3000/req",
        json={
            "phone": "+38095675432",
            "text": f"test{num}"
        },
        headers={
            "accept": "application/json",
            "api-key": "test"
        }
    ) as resp:
        print(await resp.text())
            
async def main():
    async with aiohttp.ClientSession() as session:
        one_start = time.perf_counter()
        await req(session, 0)
        one = time.perf_counter() - one_start

        all_start = time.perf_counter()
        await asyncio.gather(*(req(session, i) for i in range(100)))
        all = time.perf_counter() - all_start

        print(f"<--RESULTS-->")
        print(f"one: {one:.2f}secs")
        print(f"100 concurrent total: {all:.2f}secs")
            
import asyncio
asyncio.run(main())