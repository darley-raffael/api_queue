from asyncio import Queue
import asyncio
from datetime import datetime

from api_quote.service import send_body
from api_quote.utils.interval import calculate_interval


def producer_queue(queue: Queue, fake_data: list):
    for data in fake_data:
        queue.put_nowait(data)

    print(queue.qsize())


async def consumer_queue(name: str, queue: Queue):
    while not queue.empty():
        data = await queue.get()

        await send_body(data)

        queue.task_done()

        print(f"Task {name} done")


async def execute_queue(queue: Queue, workers: int = 2):
    now = datetime.now()
    tasks = []
    for i in range(workers):
        task = asyncio.create_task(consumer_queue(f"Task {i}", queue))
        tasks.append(task)

    await queue.join()

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks)

    print(calculate_interval(now, datetime.now()))
