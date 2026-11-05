from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Transaction:
    transaction_id: UUID
    sender_account: str
    recipient_account: str
    amount_minor: int
    currency: str = "INR"

    @classmethod
    def create(
        cls,
        sender_account: str,
        recipient_account: str,
        amount_minor: int,
    ) -> "Transaction":

        if not sender_account or not recipient_account:
            raise ValueError("Account IDs cannot be empty.")

        if sender_account == recipient_account:
            raise ValueError("Sender and recipient must be different.")

        if amount_minor <= 0:
            raise ValueError("Transfer amount must be positive.")

        return cls(
            transaction_id=uuid4(),
            sender_account=sender_account,
            recipient_account=recipient_account,
            amount_minor=amount_minor,
        )