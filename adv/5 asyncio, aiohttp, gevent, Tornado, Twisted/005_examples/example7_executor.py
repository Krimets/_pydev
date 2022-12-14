import asyncio


def highload_operation(value):
    result = 0
    for i in range(0, value):
        result += i
    return result


async def main(value):
    # виконання синхронних завдань у pool-і та отримання результату.
    result = await loop.run_in_executor(None, highload_operation, value)
    print('Result is {}'.format(result))


loop = asyncio.get_event_loop()
tasks = asyncio.wait([
    loop.create_task(main(10_000_000)),
    loop.create_task(main(10_000_001)),
])
loop.run_until_complete(tasks)
loop.close()
