import aiohttp
import asyncio


async def fetch(session, url, keyword):
    async with session.get(url, ssl=False) as response:
        text = await response.text()
        return (keyword in text, url)


async def main():
    urls = ["https://www.olx.ua", "http://example2.com"]
    keyword = "apple"

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, keyword) for url in urls]
        results = await asyncio.gather(*tasks)

        for found, url in results:
            print(f"Keyword found in {url}: {found}")

if __name__ == "__main__":
    asyncio.run(main())
