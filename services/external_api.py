
import httpx


async def get_external_posts():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://jsonplaceholder.typicode.com/posts"
        )

        response.raise_for_status()

        return response.json()
