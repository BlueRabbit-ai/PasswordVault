# Password Vault (Python CLI)

A simple command-line password manager written in Python.
It stores passwords securely, checks them against known breaches, and saves data locally in JSON format.

***

## Features

- Add, view, and delete password entries
- Passwords stored as SHA-256 hashes (no plaintext)
- Check passwords against Have I Been Pwned (k-anonymity API)
- Master password protection
- Data saved to JSON file
- Basic error handling for API failures
- Object-oriented design with inheritance

***

## Project Structure

```
password_vault/
│
├── app/
│   ├── api_client.py
│   ├── entries.py
│   ├── storage.py
│   └── vault.py
│
├── data/
│   ├── vault.json
│   └── profiles.json
│
├── main.py
├── auth.py
├── setup.py
└── README.md

classes:

VaultEntry
    └── PasswordEntry
            └── ApiEntry

```

***

## Requirements

- Python 3.10 or higher
- `requests` library

***

## Setup

Run the setup script to create a master password:

```bash
python setup.py
```

***

## Usage

Start the app:

```bash
python main.py
```

***

## Author

Student project for learning Python.