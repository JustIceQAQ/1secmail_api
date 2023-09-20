from dataclasses import dataclass


@dataclass
class Mailbox:
    id_: int  # Message id
    from_: str  # Sender email address
    subject: str  # Subject
    date: str  # Receive date

    @classmethod
    def from_dict(cls, raw_data) -> "Mailbox":
        return cls(
            id_=raw_data['id'],
            from_=raw_data['from'],
            subject=raw_data['subject'],
            date=raw_data['date']
        )


