
from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Transaction:
    transaction_id: UUID
    sender_account: str
    recipient_account: str
    amount_minor: int
    currency: str = "INR"

    def __post_init__(self):
        if not isinstance(self.transaction_id, UUID):
            raise ValueError("Transaction ID must be a valid UUID.")

        if not self.sender_account or not self.recipient_account:
            raise ValueError("Account IDs cannot be empty.")

        if self.sender_account == self.recipient_account:
            raise ValueError("Sender and recipient must be different.")

        if type(self.amount_minor) is not int or self.amount_minor <= 0:
            raise ValueError("Transfer amount must be a positive integer.")

        if not isinstance(self.currency, str) or not self.currency.strip():
            raise ValueError("Currency must be a valid non-empty string.")

    @classmethod
    def create(
        cls,
        sender_account: str,
        recipient_account: str,
        amount_minor: int,
    ) -> "Transaction":

        return cls(
            transaction_id=uuid4(),
            sender_account=sender_account,
            recipient_account=recipient_account,
            amount_minor=amount_minor,
        )
