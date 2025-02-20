# News Email Sender

## Overview

This project fetches the latest news articles about Tesla(or any other topic) using the NewsAPI and sends them via email to a specified recipient. The project consists of two Python scripts:

1. **`main.py`** - Fetches news articles and sends them via email.
2. **`sendmail.py`** - Handles sending emails securely using Gmail's SMTP server.

## Features

- Fetches the latest news articles on Tesla(Topic can be made dynamic.
- Formats and sends the top 10 articles via email.
- Uses environment variables to securely store API keys and email credentials.

## Prerequisites

- Python 3.x
- A valid API key from [NewsAPI](https://newsapi.org/)
- A Gmail account with **App Passwords** enabled (for secure authentication)

## Installation

1. Clone this repository

2. Install required dependencies:

   ```sh
   pip install requests
   ```

## Environment Variables

To enhance security, sensitive information such as API keys and email credentials are stored in environment variables. Set up the following:

**On Linux/macOS:**

```sh
export NEWS_API_KEY='your_newsapi_key'
export PYTHONEMAILPASS='your_app_password'
```

**On Windows (Command Prompt):**

```sh
set NEWS_API_KEY=your_newsapi_key
set PYTHONEMAILPASS=your_app_password
```

## Usage

1. Run the script and enter the recipient's email address when prompted:
   ```sh
   python main.py
   ```
2. The script will:
   - Fetch the latest Tesla news from NewsAPI.
   - Format the top 10 articles.
   - Send the news summary to the specified email address.

## File Structure

```
news-email-sender/
│── main.py   # Fetches news and sends email
│── sendemail.py     # Handles email sending via SMTP
│── README.md       # Project documentation
```

## Security Considerations

- **Use Environment Variables:** Storing API keys and email credentials in environment variables prevents accidental exposure.
- **Use App Passwords:** Instead of storing your actual email password, use Gmail App Passwords for secure authentication.


## Author

Mayank Kapoor

