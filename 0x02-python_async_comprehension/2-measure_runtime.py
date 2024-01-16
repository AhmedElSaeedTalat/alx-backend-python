#!/usr/bin/env python3
""" asynchronous comprehensions task """
from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ measure run time of a function"""
    start = time()
    await asyncio.gather(async_comprehension())
    end = time()
    return end - start
