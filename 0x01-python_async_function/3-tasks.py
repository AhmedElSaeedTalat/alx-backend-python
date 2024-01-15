#!/usr/bin/env python3
""" async functions tasks """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ wait random """
    task = asyncio.create_task(wait_random(max_delay))
    return task
