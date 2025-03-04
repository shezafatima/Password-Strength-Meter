# Password Strength Meter

This project is a Python application that provides a password strength meter with additional features. The application allows users to either check the strength of a password or generate a strong password using a user-friendly GUI built with Streamlit.

## Features

- **Password Strength Check:**
  - Validates that the password is at least 8 characters long.
  - Ensures the presence of both uppercase and lowercase letters.
  - Requires at least one digit and one special character from `!@#$%^&*`.
  - Implements a custom scoring system (total 5 points) with weighted checks.
  - Provides specific feedback and suggestions for improvement.
  - Includes a blacklist check against common weak passwords.

- **Password Generator:**
  - Generates a random strong password that meets all the criteria.
  - Allows users to specify a custom password length (between 8 and 32 characters).

- **User-Friendly Interface:**
  - Built with Streamlit for an interactive web-based GUI.
  - Two tabs: one for checking a password and one for generating a new password.


