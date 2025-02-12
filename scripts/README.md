# Chatbot Project

## Overview

This project is a financial chatbot that provides insights on revenue, net income, and growth for Microsoft, Apple, and Tesla.

## Screenshot

![Chatbot Interface](scripts/testbot.png)

## Files

- `scripts/chatbot.py`: The main Python script for the chatbot.
- `scripts/index.html`: The HTML interface for interacting with the chatbot.
- `data/10k filings 2022-2024 fy_updated.csv`: The CSV file containing financial data.

## How to Run

1. Ensure you have Python and Flask installed.
2. Run the Flask app:
   ```bash
   python scripts/chatbot.py
   ```
3. Open `index.html` in a web browser to interact with the chatbot.

## Limitations

- The chatbot only provides information on Microsoft, Apple, and Tesla.
- It responds to queries about revenue, net income, and growth.

## Future Improvements

- Expand to include more companies.
- Enhance natural language processing for better query understanding.
