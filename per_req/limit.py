from fastapi import Header, Body, APIRouter

from fastapi.responses import JSONResponse
from pydantic import BaseModel

import asyncio

import time

import per_req.limit_cache as limit_cache


def limit(func):
    async def wrapper(
        payload: LimitTestReq = Body(),
        api_key: str = Header()
    ):
        while True:
            async with limit_cache.reqs_lock:
                if limit_cache.reqs<50:
                    break
            await asyncio.sleep(0.01)
            
        limit_cache.reqs+=1
        resp = await func(payload, api_key)
        limit_cache.reqs-=1
        
        return resp
    
    return wrapper



router = APIRouter()



class LimitTestReq(BaseModel):
    phone: str | None = None
    text: str|None = None



@router.post(
    "/",
    summary="Send new message or reply to an existing one",
    description="This API request allows you to send an outgoing message. Only one message can be sent per request.\n\nYou can send text messages without creating a channel.",
    responses={
        200: {"description": "SUCCESS","content": {"application/json": {"example": {"status": "SUCCESS","message_id": "Message ID","description": "Message queued for sending"}}}},
        "default": {"description": "ERROR","content": {"application/json": {"example": {"status": "ERROR","description": ("Invalid user number or API key | ""Tariff expired | ""Number requires activation | ""Exceeded the limit of 100 messages on the 'Easy start' tariff | ""Receiver information not specified | ""Invalid file path| ""Message information not specified")}}}}
    }
)
@limit
async def send_msg(
    payload: LimitTestReq = Body(examples=[{
        "phone": "test phone",
        "text": "test text"
    }]),
    api_key: str = Header(description="")
):        
    if api_key != "test":
        return JSONResponse(
            status_code=401,
            content={
                "status": "ERROR",
                "description": "Invalid API key"
            }
        )
        
    await asyncio.sleep(3)
    
    return str(time.time())+payload.text