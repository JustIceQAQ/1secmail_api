import asyncio
import httpx

from lsecmail.async_helper import AsyncISecMail, AsyncISecMailEntity


async def main():
    this_async_client = httpx.AsyncClient()

    i_sec_mail = AsyncISecMail(async_client=this_async_client)
    # i_sec_mail = AsyncISecMail()

    await this_async_client.aclose()


if __name__ == '__main__':
    asyncio.run(main())
