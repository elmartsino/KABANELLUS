# Authentication Package

This package provides simple user authentication functionality in Python.

## Installation

You can install the package via pip:

```bash
pip install authentication-package
```

## Usage

Instantiate the Authentication class and use the `register` and `login` methods to handle user registration and authentication.

```python
from authentication import Authentication

# Initialize the Authentication object
auth = Authentication()

# Example usage: register a new user
print(auth.register('john_doe', 'password123'))

# Example usage: login with registered user
print(auth.login('john_doe', 'password123'))
```

## Features

- User registration with password hashing
- User login with password verification

## Dependencies

This package requires the `bcrypt` library for password hashing and verification.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
