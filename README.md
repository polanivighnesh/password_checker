# Password Complexity Checker

This Python script evaluates the strength of a password based on several criteria, such as length, usage of uppercase and lowercase letters, numbers, and special characters.

## Features

The password complexity is classified into four categories:
1. **Weak**: Password contains only letters, only numbers, or only special characters.
2. **Medium**: Password is a combination of letters and numbers.
3. **Strong**: Password is a combination of letters, numbers, and special characters.
4. **Very Strong**: Password contains uppercase letters, lowercase letters, numbers, and special characters, and is at least 16 characters long.

## Password Requirements
- Minimum length: 12 characters
- Categories:
  - Letters (Uppercase and Lowercase)
  - Numbers
  - Special characters (`!@#$%^&*(),.?":{}|<>`)

## Usage

Clone this repository and run the script as follows:

```bash
git clone https://github.com/your-username/password-checker.git
cd password-checker
python3 password_checker.py
