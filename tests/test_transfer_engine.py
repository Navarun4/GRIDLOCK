
import unittest

from backend.accounts import Account
from backend.transaction import Transaction
from backend.transfer_engine import TransferEngine


class TransferEngineTests(unittest.TestCase):

    def setUp(self):
        self.sender = Account("ACC001", "Alice", 10000)
        self.recipient = Account("ACC002", "Bob", 5000)

        self.engine = TransferEngine(
            authorization_verifier=lambda transaction: True
        )

        self.engine.register_account(self.sender)
        self.engine.register_account(self.recipient)

        self.transaction = Transaction.create(
            "ACC001",
            "ACC002",
            2500
        )

    def test_successful_transfer(self):
        self.engine.execute_transfer(self.transaction)

        self.assertEqual(self.sender.balance_minor, 7500)
        self.assertEqual(self.recipient.balance_minor, 7500)

    def test_unauthorized_transfer_is_rejected(self):
        engine = TransferEngine(
            authorization_verifier=lambda transaction: False
        )

        engine.register_account(self.sender)
        engine.register_account(self.recipient)

        with self.assertRaises(PermissionError):
            engine.execute_transfer(self.transaction)

        self.assertEqual(self.sender.balance_minor, 10000)
        self.assertEqual(self.recipient.balance_minor, 5000)

    def test_replayed_transaction_is_rejected(self):
        self.engine.execute_transfer(self.transaction)

        with self.assertRaises(ValueError):
            self.engine.execute_transfer(self.transaction)

        self.assertEqual(self.sender.balance_minor, 7500)
        self.assertEqual(self.recipient.balance_minor, 7500)


if __name__ == "__main__":
    unittest.main()
