import datetime

from lsecmail.schemas import EmailAddresses, MailBox, Message, Attachment


def test_email_addresses_base_model_init():
    this_email = "qq@qq.com"
    this_email_login, this_email_domain = this_email.split("@")
    result = EmailAddresses(email=this_email)
    assert result.email == this_email
    assert result.login == this_email_login
    assert result.domain == this_email_domain


def test_mail_box_base_model_init():
    this_mail = {
        "id": 639,
        "from": "someone@example.com",
        "subject": "Some subject",
        "date": "2018-06-08 14:33:55"
    }
    mail = MailBox.model_validate(this_mail)
    assert mail.id_ == this_mail.get("id")
    assert mail.from_ == this_mail.get("from")
    assert mail.subject == this_mail.get("subject")
    assert mail.date == datetime.datetime.strptime(this_mail.get("date"), "%Y-%m-%d %H:%M:%S")


def test_attachment_base_model_init():
    this_attachment = {
        "filename": "iometer.pdf",
        "contentType": "application\/pdf",
        "size": 47412
    }
    attachment = Attachment.model_validate(this_attachment)
    assert attachment.filename == this_attachment.get("filename")
    assert attachment.content_type == this_attachment.get("contentType")
    assert attachment.size == this_attachment.get("size")


def test_message_base_model_init():
    this_message = {
        "id": 639,
        "from": "someone@example.com",
        "subject": "Some subject",
        "date": "2018-06-08 14:33:55",
        "attachments": [{
            "filename": "iometer.pdf",
            "contentType": "application/pdf",
            "size": 47412
        }],
        "body": "Some message body\n\n",
        "textBody": "Some message body\n\n",
        "htmlBody": ""
    }
    message = Message.model_validate(this_message)
    assert message.id_ == this_message.get("id")
    assert message.from_ == this_message.get("from")
    assert message.subject == this_message.get("subject")
    assert message.date == datetime.datetime.strptime(this_message.get("date"), "%Y-%m-%d %H:%M:%S")

    assert message.body == this_message.get("body")
    assert message.text_body == this_message.get("textBody")
    assert message.html_body == this_message.get("htmlBody")

    assert message.attachments[0] == Attachment.model_validate(this_message.get("attachments")[0])
