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
