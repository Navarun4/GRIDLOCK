from threading import RLock
from typing import Callable

from backend.accounts import Account
from backend.transaction import Transaction


class TransferEngine:
    def __init__(
        self,
        authorization_verifier: Callable[[Transaction], bool],
    ):
        self.accounts: dict[str, Account] = {}
        self.executed_transactions: set[str] = set()
        self.authorization_verifier = authorization_verifier
        self._lock = RLock()

    def register_account(self, account: Account) -> None:
        with self._lock:
            if account.account_id in self.accounts:
                raise ValueError("Account already exists.")

            self.accounts[account.account_id] = account

    def execute_transfer(self, transaction: Transaction) -> str:
        with self._lock:
            transaction_id = str(transaction.transaction_id)

            if transaction_id in self.executed_transactions:
                raise ValueError("Transaction has already been executed.")

            sender = self.accounts.get(transaction.sender_account)
            recipient = self.accounts.get(transaction.recipient_account)

            if sender is None or recipient is None:
                raise ValueError("Account not found.")

            if sender.currency != recipient.currency:
                raise ValueError("Account currencies do not match.")

            if sender.currency != transaction.currency:
                raise ValueError("Transaction currency does not match.")

            if sender.balance_minor < transaction.amount_minor:
                raise ValueError("Insufficient funds.")

            # Fail closed: no transfer without verified authorization.
            if not self.authorization_verifier(transaction):
                raise PermissionError("Transaction authorization denied.")

            # Both balance changes happen under the same lock.
            sender.balance_minor -= transaction.amount_minor
            recipient.balance_minor += transaction.amount_minor

            self.executed_transactions.add(transaction_id)

            return transaction_id