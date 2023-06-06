import asyncio
import time
from http_utils import perform_get_request
from ParseUsers import User
USERS_URL = "https://jsonplaceholder.typicode.com/users"

def get_username_sync():
    start_time = time.perf_counter()
    response_list = perform_get_request(USERS_URL)
    elapsed = time.perf_counter() - start_time
    print(f"Execution time for sync call {elapsed:0.2f}")
    for response in response_list:
        user = User(response)
        print(user.username, user.name, user.email)

async def get_username_async():
    start_time = time.perf_counter()
    response_list = await perform_get_request_async(USERS_URL)
    elapsed = time.perf_counter() - start_time
    print(f"Execution time for async call {elapsed:0.2f}")
    for response in response_list:
        user = User(response)
        print(user.username, user.name, user.email)

async def perform_get_request_async(url):
    loop = asyncio.get_event_loop()
    response_list = await loop.run_in_executor(None, perform_get_request, url)
    return response_list


if __name__ == "__main__":
    get_username_sync()
    asyncio.run(get_username_async())