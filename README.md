# GRIDLOCK
### Defensive Transaction Authorization & Security Platform

Gridlock is an experimental security project exploring how sensitive financial actions can remain protected even when account credentials are compromised.

Its central principle is simple:

**Possession of credentials must not automatically grant authority to perform sensitive actions.**

## The Problem

Compromised credentials can allow attackers to initiate unauthorized financial transactions. Gridlock explores an additional layer of transaction-specific authorization to help prevent this.

## Current Implementation

The initial prototype includes:

- **Transaction Model:** Validated transaction objects with unique UUIDs.
- **Account Model:** Account representation with balance and currency information.
- **Transfer Engine:** Handles transfers between registered accounts.
- **Authorization Verification:** Rejects transactions without successful authorization.
- **Replay Protection:** Prevents an already-executed transaction ID from being reused.
- **Security Tests:** Tests for invalid transactions, unauthorized transfers, replay attempts and successful execution.

## Planned Architecture

- **Trusted-Device Cryptographic Approval:** Transaction-specific approval using established cryptographic standards.
- **AEGIS:** An AI-assisted threat intelligence and risk analysis component.
- **Pandora's Box:** A defensive containment and incident-response component.

These components are planned and are not yet implemented.

## Technology

- Python
- Git and GitHub
- Python unittest framework

## Running the Tests

On Windows, from the project root:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Development Status

**Phase 1 — Foundation and Architecture**

The initial transaction models, transfer engine, authorization checks and foundational security tests are implemented.

## Security Scope

- Synthetic accounts and transactions only.
- No connection to real banking systems.
- Established cryptographic standards rather than custom cryptography.
- Security testing before feature expansion.
- Not intended for production financial use.

## Vision

Gridlock aims to explore a stronger model of digital transaction security where authentication, authorization and transaction approval are treated as distinct security responsibilities.

*Built as an ongoing independent engineering project.*