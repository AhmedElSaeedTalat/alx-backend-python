#!/usr/bin/env python3
""" async functions tasks """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ raturn list of all delays """
    floats_list = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        returned_value = await task
        floats_list.append(returned_value)
    return sorted(floats_list)
