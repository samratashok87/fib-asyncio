#!/usr/bin/env python3

import asyncio
import random


async def fib(number: int) -> int:
    await asyncio.sleep(random.randint(0, 1))
    if number <= 1:
        return number
    fib_n_minus_one = await fib(number - 1)
    fib_n_minus_two = await fib(number - 2)
    return fib_n_minus_one + fib_n_minus_two


async def main(number: int):
    fib_task_1 = asyncio.create_task(fib(number), name='Fib Task 1')
    fib_task_2 = asyncio.create_task(fib(number), name='Fib Task 2')

    pending = [fib_task_1, fib_task_2]
    while pending:
        done, pending = await asyncio.wait(
                                        pending,
                                        return_when=asyncio.FIRST_COMPLETED
                                        )
        done_task = done.pop()
        result = done_task.result()
        print(f'Completed Task {done_task.get_name()}')
        print(f'Result From Task {done_task.get_name()} : {result}')


if __name__ == '__main__':
    import sys
    number = int(sys.argv[1])
    asyncio.run(main(number))
