#!/usr/bin/env python3
""" async functions tasks """
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures time of a function execution """
    begin = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    total = end - begin
    return total / n
