import asyncio


async def async_worker(number, divider):
    """
    замість yield/yield from використовуємо синтаксис async/await.
    """
    print('Worker {} started'.format(number))
    await asyncio.sleep(2)
    print(number / divider)
    return number / divider


async def gather_worker():
    # виконання кількох завдань та отримання результату від кожної з них
    # в результаті виконання ми отримаємо список результатів у тому ж порядку,
    # у якому передавали співпрограми.
    result = await asyncio.gather(
        async_worker(50, 10),
        async_worker(60, 10),
        async_worker(70, 10),
        async_worker(80, 10),
        async_worker(90, 10),
    )
    print(result)


event_loop = asyncio.get_event_loop()
task_list = [
    # async_worker(30, 10),
    # asyncio.ensure_future(async_worker(30, 10)),
    event_loop.create_task(gather_worker())
]
tasks = asyncio.wait(task_list)
event_loop.run_until_complete(tasks)
event_loop.close()
