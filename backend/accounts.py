from dataclasses import dataclass


@dataclass
class Account:
    account_id: str
    owner: str
    balance_minor: int
    currency: str = "INR"

    def __post_init__(self):
        if not self.account_id:
            raise ValueError("Account ID cannot be empty.")

        if not self.owner:
            raise ValueError("Account owner cannot be empty.")

        if self.balance_minor < 0:
            raise ValueError("Account balance cannot be negative.")