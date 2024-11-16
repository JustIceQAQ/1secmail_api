import pytest
from pydantic import BaseModel


class Login(BaseModel):
    login: str
    domain: str
    message_id: int
    filename: str


@pytest.fixture(scope='session')
def get_login() -> Login:
    return Login(login="qaq", domain="1secmail.com", message_id=995855847, filename="serverqaq88.png")
