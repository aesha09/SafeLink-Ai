# Smart URL Vulnerability Scanner

Backend Flask app for scanning URLs using multiple tools and APIs.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask app:
   ```
   python app.py
   ```

## Features

- WHOIS lookup
- Nmap port scanning
- VirusTotal API scanning
- Google Safe Browsing API
- Image EXIF metadata extraction
- SQLite for scan history