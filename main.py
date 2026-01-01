import uvicorn

from fastapi import FastAPI

from limit import limit_router



async def main():
    app = FastAPI(title="Vladik TG API")
    
    app.include_router(limit_router, prefix="/", tags=["limit"])


    config = uvicorn.Config(
        app=app,
        # host="127.1.5.176",
        port=3000,
        log_level="info",
    )

    server = uvicorn.Server(config)
    await server.serve()
    
import asyncio
asyncio.run(main())