from fastapi import Header, Body, APIRouter

from fastapi.responses import JSONResponse
from pydantic import BaseModel

import asyncio



req_countdown_per_sec = 0
last_update = None

def limit():
    pass



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
async def send_msg(
    payload: LimitTestReq = Body(example={
        "phone": "test phone",
        "text": "test text"
    }),
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
    
    return "hello"