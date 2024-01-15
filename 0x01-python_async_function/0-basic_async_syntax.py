#!/usr/bin/env python3
""" async functions tasks """
import asyncio
import random


async def wait_random(max_delay=10):
    """ wait random number using random.uniform """
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
