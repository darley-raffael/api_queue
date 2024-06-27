import asyncio
from fastapi import FastAPI
from httpx import request

from api_quote.fake_data import get_fake_data
from api_quote.print_name import print_name
from api_quote.service import request_data, send_body
from api_quote.service_queue import execute_queue, producer_queue


app = FastAPI()
body_queue = asyncio.Queue()


@app.get("/")
async def hello():
    asyncio.create_task(print_name())
    return {"message": "Hello World"}


@app.get("/send")
async def send_data():
    asyncio.create_task(request_data())
    return {"message": "sended"}


@app.get("/send_body")
async def send_body_data():
    list_data = get_fake_data()
    producer_queue(body_queue, list_data)
    asyncio.create_task(execute_queue(body_queue, 5))
    return {"message": "sended"}
