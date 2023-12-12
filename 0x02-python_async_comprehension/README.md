0x02. Python - Async Comprehension
Python
Back-end
This directory will be dealing with tasks on python async comprehensions.
The following are what we are going to delving into:
1. How to write an asynchronous generator:
    -> An asynchronous generator is a special kind of coroutine that produces a sequence of values asynchronously using the async def syntax. To define an asynchronous generator, you can use the async def statement along with the yield keyword to produce values asynchronously.

Here's an example:
import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate an asynchronous operation
        yield i

In this example, async_generator is an asynchronous generator that produces values from 0 to 4 asynchronously with a sleep of 1 second between each value using await asyncio.sleep(1)

2. How to use async comprehensions:
    -> Async comprehensions allow you to create asynchronous sequences using a concise syntax. It is similar to list comprehensions but with async for syntax.

Here's an example of an async comprehension:
import asyncio

async def fetch_data(url):
    # Simulated data fetching from a URL
    await asyncio.sleep(1)
    return f"Data from {url}"

async def fetch_multiple_data(urls):
    results = [await fetch_data(url) async for url in urls]
    return results

urls = ['url1', 'url2', 'url3']
results = asyncio.run(fetch_multiple_data(urls))
print(results)

In this example, fetch_multiple_data fetches data from multiple URLs asynchronously using async comprehensions. The await fetch_data(url) is used inside the comprehension to await the result from each URL.

3. How to type-annotate generators:
Python allows type hinting to specify the types of variables, function parameters, and return values. To type-annotate generators, you can use the typing module to specify the types of yielded values.

Here's an example:
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[int, None]:
    for i in range(5):
        yield i

In this example, AsyncGenerator[int, None] is used as the return type hint, where int represents the type of values yielded by the generator, and None represents the type of the value returned when the generator is exhausted.

Using type hints in this way helps improve code readability and enables type checkers to catch potential errors in your code.
