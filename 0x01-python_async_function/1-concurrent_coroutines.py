#!/usr/bin/env python3
""" async functions tasks """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ raturn list of all delays """
    tasks_list = []
    for i in range(n):
        tasks_list.append(asyncio.ensure_future(wait_random(max_delay)))
    all_values = []
    for completed in asyncio.as_completed(tasks_list):
        val = await completed
        all_values.append(val)
    return all_values
