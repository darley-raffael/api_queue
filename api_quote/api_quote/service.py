import json
import time
from httpx import AsyncClient
from datetime import datetime

from api_quote.fake_data import get_fake_data
from api_quote.utils.interval import calculate_interval


async def send_body(data: dict):
    payload = json.dumps(data)
    headers = {"Content-Type": "application/json"}

    async with AsyncClient(timeout=10) as client:
        response = await client.post(
            "http://localhost:3000", data=payload, headers=headers
        )

        print(response)


async def request_data():
    now = datetime.now()
    lista_data = get_fake_data()

    for data in lista_data:
        await send_body(data)

    print(calculate_interval(now, datetime.now()))
