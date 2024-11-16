from typing import Any

import httpx
from ..schemas import EmailAddresses, MailBox, Message

ROOT_PATH = "https://www.1secmail.com/api/v1/"


class ISecMail:
    """
    https://www.1secmail.com/api/
    """
    root_path = ROOT_PATH

    def __init__(self):
        self.client = httpx.Client(timeout=None)

    def gen_random_mailbox(self, count: int | None = 5) -> list[EmailAddresses]:
        response = self.client.get(f"{self.root_path}?action=genRandomMailbox&count={count}")
        response.raise_for_status()
        return [EmailAddresses(email=email) for email in response.json()]

    def get_domain_list(self) -> list[str]:
        response = self.client.get(f"{self.root_path}?action=getDomainList")
        response.raise_for_status()
        return response.json()

    def get_messages(self, login: str, domain: str) -> list[MailBox]:
        response = self.client.get(f"{self.root_path}?action=getMessages&login={login}&domain={domain}")
        response.raise_for_status()
        return [MailBox.model_validate(message) for message in response.json()]

    def read_message(self, login: str, domain: str, message_id: int) -> Message:
        response = self.client.get(f"{self.root_path}?action=readMessage&login={login}&domain={domain}&id={message_id}")
        response.raise_for_status()
        return Message.model_validate(response.json())

    def download_attachment(self, login: str, domain: str, message_id: int, filename: str) -> bytes:
        response = self.client.get(
            f"{self.root_path}?action=download&login={login}&domain={domain}&id={message_id}&file={filename}"
        )
        response.raise_for_status()
        return response.content
