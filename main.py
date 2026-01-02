import uvicorn

from fastapi import FastAPI

from per_sec.limit import router as limit_router

import per_sec.limit_cache

async def main():
    asyncio.create_task(init())
    app = FastAPI(title="Vladik TG API")
    
    app.include_router(limit_router, tags=["limit"])


    config = uvicorn.Config(
        app=app,
        # host="127.1.5.176",
        port=3000,
        log_level="info",
    )

    server = uvicorn.Server(config)
    await server.serve()
    
async def init():
    while True:
        await asyncio.sleep(1)
        async with per_sec.limit_cache.reqs_lock:
            per_sec.limit_cache.reqs_per_interval = 10
    
import asyncio
asyncio.run(main())