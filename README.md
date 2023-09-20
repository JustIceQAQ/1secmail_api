# Minimum 1secmail API

---

## Source

- https://www.1secmail.com/api/

---

## Class Method

- there have sync and async version~

- class ISecMail
    - Generating random email addresses
        - .gen_random_mail_box(count: int = 1) -> list[ISecMailEntity]
    - Getting list of active domains
        - .get_domain_list() -> list[str]
- class ISecMailEntity
    - Open mail in www.1secmail.com website
        - .open_in_browser()
    - Checking your mailbox
        - .get_messages() -> list[dict]
    - Fetching single message
        - .read_message(mail_id: Union[int, str]) -> dict
    - Attachment download
        - .download_file(mail_id: Union[int, str], filename: str) -> bytes
    

