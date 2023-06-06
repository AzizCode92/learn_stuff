import asyncio
from http_utils import fetch_url, POST_URL, COMMENT_URL


async def one_async_task():
    """
    Creates a single asyncio task
    """
    task = asyncio.create_task(fetch_url(POST_URL))
    result = await task
    print(result)


async def multiple_async_task():
    """
    Creates multiple asyncio tasks
    """
    tasks = [
        asyncio.create_task(fetch_url(POST_URL)),
        asyncio.create_task(fetch_url(COMMENT_URL))
    ]
    results = await asyncio.gather(*tasks)
    posts, comments = results
    print(posts, comments)


if __name__ == "__main__":
    # Run the event loop
    asyncio.run(one_async_task())
    asyncio.run(multiple_async_task())
