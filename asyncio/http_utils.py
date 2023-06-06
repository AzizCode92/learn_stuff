import requests
import aiohttp

POST_URL = "https://jsonplaceholder.typicode.com/posts"
COMMENT_URL = "https://jsonplaceholder.typicode.com/comments"

def perform_get_request(url):
    """
    Sends a GET request to the specified URL and returns the response content as JSON if successful.

    :param url: The URL to fetch.
    :type url: str
    :return: The JSON response if the request is successful, else None.
    :rtype: dict or list or None
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any unsuccessful status code
        return response.json()  # Parse the response content as JSON
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
async def fetch_url(url):
    async with aiohttp.client.ClientSession() as cs:
        async with cs.get(url) as response:
            posts = await response.json()
            return posts
