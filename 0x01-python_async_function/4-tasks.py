#!/usr/bin/env python3
""" async functions tasks """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ resolve tasks and return result once completed """
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    results = []
    for completed in asyncio.as_completed(tasks):
        result = await completed
        results.append(result)
    return results
