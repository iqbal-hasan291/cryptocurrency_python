# import libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import requests
import schedule
from datetime import datetime
import time
import pandas as pd

def send_mail(subject,body,filename): # function to send email
    
    #setup mail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_mail = 'iqbalhasanmbstu.1998@gmail.com'
    sender_password = 'Gmail Password' # use app password if 2FA is enabled
    receiver_mail = 'iqbalmath.291@gmail.com'

    #compose mail
    message = MIMEMultipart()
    message["From"] = sender_mail
    message["To"] = receiver_mail
    message["Subject"] = subject
    
    #attach body
    message.attach(MIMEText(body , "plain"))
    
    #attach CSV file
    with open (filename , 'rb') as file:
        part=MIMEBase ('application' , 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header ('Content-Disposition' , f'attachment; filename="{filename}"')
        message.attach(part)
        
    # start server and send email    
    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls()
            server.login(sender_mail,sender_password)
            server.sendmail(sender_mail,receiver_mail,message.as_string())
            print("Email sent successfully")

    except Exception as e:
        print(f'unable to send mail {e}')    
        
# Function to get cryptocurrency data from CoinGecko API        
def get_crypto_data():
    
    #api information
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    param = {
        'vs_currency' : 'usd',
        'order' : 'market_cap_desc',
        'per_page': 250,
        'page': 1
    }

    #sending response
    response=requests.get(url , params=param)
    
    if response.status_code==200:
        print('Connection Successful!\nGetting the Data')

        # if connection is successful, parse the response
        data=response.json()
        
        # create a DataFrame from the data
        df=pd.DataFrame(data)
        
        # select relevant columns
        df = df[[
            'id','current_price', 'market_cap', 'price_change_percentage_24h',
            'high_24h', 'low_24h','ath', 'atl',
        ]]
        
        
        # create columns for better readability
        today=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        df['time_stamp'] = today
        
        # negetive and positive price change
        top_negative_10 = df.nsmallest(10, 'price_change_percentage_24h')
        
        top_positive_10 = df.nlargest(10, 'price_change_percentage_24h') 
        
        # save the DataFrame to a CSV file
        filename = f'crypto_data_{today}.csv'
        print(f'Saving data to {filename}...')
        df.to_csv(filename, index=False)
        print(f'Data saved to {filename}')
        
        subject = 'Crypto Currency Data'
        body = f"""
        Good Day!\n\n
        your crypto currency data is ready.\n\n
        Please find the attached file for details.\n\n

        Top 10 Cryptocurrencies with Highest Price Change (24h):\n
        {top_positive_10}\n\n\n  

        Top 10 Cryptocurrencies with Lowest Price Change (24h):
        {top_negative_10}\n\n\n 
        
        Best Regards,\n
        Crypto Currency Bot
        See you soon!
        """
        send_mail(subject, body, filename)
    else:
        print(f'Connection failed Error Code {response.status_code}')
        
        
# end of get_crypto_data function        
if __name__ == "__main__":
    # schedule the job to run every day at 9:00 AM
    schedule.every().day.at("00:49").do(get_crypto_data)
    
    while True:
        schedule.run_pending()
        time.sleep(60) # wait for one minute before checking again
        
        
        
        
    
    