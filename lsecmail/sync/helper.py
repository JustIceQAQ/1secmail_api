import httpx
from ..schemas import EmailAddresses

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
