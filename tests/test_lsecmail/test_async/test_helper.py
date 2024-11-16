import pytest

from lsecmail.async_ import ISecMail
from lsecmail.schemas import EmailAddresses, MailBox, Message


@pytest.mark.asyncio
def test_import():
    from lsecmail.sync import ISecMail  # noqa
    from lsecmail.sync.helper import ISecMail  # noqa


@pytest.mark.asyncio
async def test_gen_random_mailbox():
    isecmail = ISecMail()
    emails = await isecmail.gen_random_mailbox(count=1)
    assert len(emails) == 1
    for email in emails:
        assert isinstance(email, EmailAddresses)


@pytest.mark.asyncio
async def test_get_domain_list():
    isecmail = ISecMail()
    domain_list = await isecmail.get_domain_list()
    assert isinstance(domain_list, list)


@pytest.mark.asyncio
async def test_get_messages(get_login):
    isecmail = ISecMail()
    messages = await isecmail.get_messages(login=get_login.login, domain=get_login.domain)
    assert isinstance(messages, list)
    for message in messages:
        assert isinstance(message, MailBox)


@pytest.mark.asyncio
async def test_read_message(get_login):
    isecmail = ISecMail()
    messages = await isecmail.read_message(login=get_login.login, domain=get_login.domain,
                                           message_id=get_login.message_id)
    assert isinstance(messages, Message)


@pytest.mark.asyncio
async def test_download_attachment(get_login):
    isecmail = ISecMail()
    attachment = await isecmail.download_attachment(login=get_login.login, domain=get_login.domain,
                                                    message_id=get_login.message_id,
                                                    filename=get_login.filename)
    assert isinstance(attachment, bytes)
