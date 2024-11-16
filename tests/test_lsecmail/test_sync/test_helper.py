from lsecmail.sync import ISecMail
from lsecmail.schemas import EmailAddresses


def test_import():
    from lsecmail.sync import ISecMail  # noqa
    from lsecmail.sync.helper import ISecMail  # noqa


def test_gen_random_mailbox():
    isecmail = ISecMail()
    emails = isecmail.gen_random_mailbox(count=1)
    assert len(emails) == 1
    for email in emails:
        assert isinstance(email, EmailAddresses)
