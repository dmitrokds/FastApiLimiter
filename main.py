import uvicorn

from fastapi import FastAPI

from per_sec.limit import router as per_sec_limit_router
import per_sec.limit_cache


from per_req.limit import router as per_req_limit_router



async def init_limit_per_sec_updater():
    while True:
        await asyncio.sleep(1)
        async with per_sec.limit_cache.reqs_lock:
            per_sec.limit_cache.reqs_per_interval = 10
            
            
            
            

async def main():
    # -- Limit per sec
    asyncio.create_task(init_limit_per_sec_updater())
    
    app = FastAPI(title="Vladik TG API")
    
    app.include_router(per_sec_limit_router, prefix="/sec", tags=["sec limit"])
    app.include_router(per_req_limit_router, prefix="/req", tags=["req limit"])


    config = uvicorn.Config(
        app=app,
        port=3000,
        log_level="info",
    )

    server = uvicorn.Server(config)
    await server.serve()
    
    
import asyncio
asyncio.run(main())
