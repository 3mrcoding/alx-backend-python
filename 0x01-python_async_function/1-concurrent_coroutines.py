#!/usr/bin/env python3
"""coroutines"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """coroutine that call wait_random n times"""
    list: List[float] = []

    for i in range(n):
        list.append(await wait_random(max_delay))

    return sorted(list)
