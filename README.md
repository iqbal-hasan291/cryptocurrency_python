# Crypto Currency Tracker and Email Automation

This project is a Python-based automation tool that collects real-time cryptocurrency market data using the CoinGecko API, analyzes the data to identify the top 10 gainers and losers in the last 24 hours, and sends the results as an email with an attached CSV file every day at a scheduled time (default: 9:00 AM).

It is designed for anyone interested in automating crypto market monitoring and email reporting using Python and open APIs.

![](https://github.com/iqbal-hasan291/cryptocurrency_python/blob/65398dac76414d83c0ed29a1d5c6b68cc0563867/image/AutomatableTasks.jpg)

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

![](https://github.com/iqbal-hasan291/cryptocurrency_python/blob/712cc216297382a0ae67033874b2e2915c010047/image/Crypto%20Currency%20Tracker%20and%20Email%20Automation%20-%20visual%20selection.png)

---
##  Scheduling

schedule.every().day.at("09:00").do(get_crypto_data)

---

##  Output

- CSV file named like: `crypto_data_01-07-2025 09-00-00.csv`
- Email body includes:
  - 📈 Top 10 cryptocurrencies by price gain (24h)
  - 📉 Top 10 cryptocurrencies by price drop (24h)


## Sample Output

![](https://github.com/iqbal-hasan291/cryptocurrency_python/blob/5a7ac1ae73382cdb41186b9446b571b1f1454821/image/Email%201.png)

![](https://github.com/iqbal-hasan291/cryptocurrency_python/blob/5a7ac1ae73382cdb41186b9446b571b1f1454821/image/Email%202.png)

---

## Make sure to:
- Enable **Less Secure App Access** or use **App Passwords** if you have 2FA enabled.
- Update the script with your email credentials:
  ```python
  sender_mail = 'your_email@gmail.com'
  sender_password = 'your_app_password'
  receiver_mail = 'receiver_email@gmail.com'


### Thank You
