# Crypto Currency Tracker and Email Automation

This project is a Python-based automation tool that collects real-time cryptocurrency market data using the CoinGecko API, analyzes the data to identify the top 10 gainers and losers in the last 24 hours, and sends the results as an email with an attached CSV file every day at a scheduled time (default: 9:00 AM).

It is designed for anyone interested in automating crypto market monitoring and email reporting using Python and open APIs.

---

## Project Features

- Fetches up-to-date cryptocurrency data from the CoinGecko API.
- Analyzes the 24-hour price change percentage to determine:
  - Top 10 cryptocurrencies with the highest gains.
  - Top 10 cryptocurrencies with the most significant losses.
- Saves the complete market data with a timestamp to a CSV file.
- Automatically sends the CSV file and summary via email to the user.
- Uses Python's built-in modules and lightweight libraries to avoid heavy dependencies.
- Fully automated with daily scheduling using the `schedule` module.

---

## Technologies Used

- **Python**: Programming language used for the entire workflow.
- **Pandas**: Data analysis and manipulation.
- **Requests**: Handling API calls.
- **Schedule**: Job scheduling for daily execution.
- **Smtplib, Email Modules**: Sending formatted emails with attachments.

---

## How It Works

1. **Fetch Data**: The script requests real-time cryptocurrency market data from the CoinGecko API.
2. **Analyze Data**: Using Pandas, it calculates the top 10 currencies with the highest and lowest price change in the last 24 hours.
3. **Save Results**: A CSV file is created containing the full dataset, with a timestamp in the filename for record-keeping.
4. **Email Report**: An email is generated and sent to the receiver, containing a brief summary of the top 10 performers and losers, along with the CSV file attached.
5. **Scheduled Execution**: The script runs automatically every day at a specific time using the `schedule` library.

---
##  Scheduling

schedule.every().day.at("09:00").do(get_crypto_data)

---

##  Output

- CSV file named like: `crypto_data_01-07-2025 09-00-00.csv`
- Email body includes:
  - 📈 Top 10 cryptocurrencies by price gain (24h)
  - 📉 Top 10 cryptocurrencies by price drop (24h)
