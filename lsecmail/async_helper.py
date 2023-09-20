import abc
import webbrowser
from typing import Union, Optional
import httpx

ROOT_PATH = "https://www.1secmail.com/api/v1/"


class Init(abc.ABC):
    async def _httpx_client(self, url: str) -> httpx.Response:
        if self._is_external_async_client:
            return await self._async_client.get(url)
        async with httpx.AsyncClient() as client:
            return await client.get(url)


class AsyncISecMailEntity(Init):
    """
    https://www.1secmail.com/api/
    """
    root_path = ROOT_PATH

    @classmethod
    def from_this(cls, email: str) -> "AsyncISecMailEntity":
        _login, domain = email.split("@")
        return cls(_login, domain)

    def __init__(self, login: str, domain: str, async_client: Optional[httpx.AsyncClient] = None):
        """
        Initialization Entity
        :param login: username
        :param domain: domain
        """
        self.login = login
        self.domain = domain
        self.path = f"{self.root_path}?login={self.login}&domain={self.domain}"
        self._is_external_async_client = async_client is not None
        self._async_client: Optional[httpx.AsyncClient] = async_client

    def __repr__(self):
        return f"ISecMailEntity<{self.login}@{self.domain}>"

    def open_in_browser(self) -> None:
        """
        Open mail in www.1secmail.com website
        :return:
        """
        webbrowser.open(f'https://www.1secmail.com/?login={self.login}&domain={self.domain}', new=2)

    async def get_messages(self) -> list[dict]:
        """
        Checking your mailbox:
        To check and get a list of emails for a mailbox.
        :return: List with Mailbox messages
        """

        response = await self._httpx_client(f"{self.path}&action=getMessages")
        return response.json()

    async def read_message(self, mail_id: Union[int, str]) -> dict:
        """
        Fetching single message:
        Now you can fetch single message with another API call:
        :param mail_id: message id
        :return: Dict with mail messages
        """
        response = await self._httpx_client(
            f"{self.path}&action=readMessage&id={mail_id}"
        )
        return response.json()

    async def download_file(self, mail_id: Union[int, str], filename: str) -> bytes:
        """
        Attachment download:
        To download attachment from message:
        :param mail_id: message id
        :param filename: filename of attachment
        :return: Bytes with file
        """
        response = await self._httpx_client(
            f"{self.path}&action=download&id={mail_id}&file={filename}"
        )
        return response.content


class AsyncISecMail(Init):
    """
    https://www.1secmail.com/api/
    """
    root_path = ROOT_PATH

    def __init__(self, async_client: Optional[httpx.AsyncClient] = None):
        self._is_external_async_client = async_client is not None
        self._async_client: Optional[httpx.AsyncClient] = async_client

    async def gen_random_mail_box(self, count: int = 1) -> list[AsyncISecMailEntity]:
        """
        Generating random email addresses:
        This is NOT required. You can use any email address with our domains without generating it before.
        Just think your username@our_domains and use it anywhere.
        Our server are always ready to receive message for any email address.
        This function just generate random 6-12 character username and add to it one of our latest domains.
        You can generate any numer of emails at once
        :param count: (optional)
        :return: List with AsyncISecMailEntity email addresses
        """
        response = await self._httpx_client(f"{self.root_path}?action=genRandomMailbox&count={count}")
        return list(map(AsyncISecMailEntity.from_this, response.json()))

    async def get_domain_list(self) -> list[str]:
        """
        Getting list of active domains:
        This function generate list of currently active domains
        on which our system is handling incoming emails at the moment
        :return: List with domains
        """
        response = await self._httpx_client(f"{self.root_path}?action=getDomainList")
        return response.json()
