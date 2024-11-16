from lsecmail.schemas import EmailAddresses


def test_base_model():
    this_email = "qq@qq.com"
    this_email_login, this_email_domain = this_email.split("@")
    result = EmailAddresses(email=this_email)
    assert result.email == this_email
    assert result.login == this_email_login
    assert result.domain == this_email_domain
