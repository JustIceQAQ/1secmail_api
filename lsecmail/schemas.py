import datetime
from typing import Any

from pydantic import BaseModel, Field, model_validator, EmailStr


class EmailAddresses(BaseModel):
    email: EmailStr
    login: str | None = Field(default=None)
    domain: str | None = Field(default=None)

    @model_validator(mode="after")
    def split_email(cls, value: "EmailAddresses"):
        email = value.email
        if "@" in email:
            login, domain = email.split("@")
            value.login = login
            value.domain = domain
        return value


class MailBox(BaseModel):
    id_: int = Field(alias="id")
    from_: EmailStr = Field(alias="from")
    subject: str
    date: str | datetime.datetime

    @model_validator(mode="after")
    def format_date(cls, value: "MailBox"):
        date_string = value.date
        value.date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        return value


class Attachment(BaseModel):
    filename: str
    content_type: str = Field(alias="contentType")
    size: int


class Message(BaseModel):
    id_: int = Field(alias="id")
    from_: EmailStr = Field(alias="from")
    subject: str
    date: str | datetime.datetime
    attachments: list[Attachment] = Field(default_factory=list)
    body: str
    text_body: str = Field(alias="textBody")
    html_body: str = Field(alias="htmlBody")

    @model_validator(mode="after")
    def format_date(cls, value: "MailBox"):
        date_string = value.date
        value.date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        return value
