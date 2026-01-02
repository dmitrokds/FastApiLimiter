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
        t0 = time.perf_counter()
        await req(session, 0)
        single = time.perf_counter() - t0

        t1 = time.perf_counter()
        await asyncio.gather(*(req(session, i) for i in range(100)))
        total = time.perf_counter() - t1

        print(f"single: {single:.4f}s")
        print(f"100 concurrent total: {total:.4f}s")
        print(f"ratio total/single: {total/single:.2f}x")
            
import asyncio
asyncio.run(main())