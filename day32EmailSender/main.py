password=''
email=''
import smtplib
import pandas
import datetime
import random
now=datetime.datetime.now()
day_of_week=now.weekday()

data=pandas.read_csv("quotes.txt")

a=data.values.tolist()
msg=random.choice(a)
msg=" ".join(msg)

if day_of_week==1:

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs="vanshikasaxena0207@gmail.com",msg=f"Subject:Quote of the week\n\n {msg}")

