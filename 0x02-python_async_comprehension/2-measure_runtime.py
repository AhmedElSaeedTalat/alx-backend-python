#!/usr/bin/env python3
""" asynchronous comprehensions task """
from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure run time of a function"""
    start = time()
    called_functions = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*called_functions)
    end = time()
    return end - start
