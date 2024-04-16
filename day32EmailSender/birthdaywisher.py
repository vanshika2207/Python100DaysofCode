##################### Extra Hard Starting Project ######################
import datetime
import pandas as pd
import smtplib
import random

password=''
email=''
now=datetime.datetime.now().date()
now=str(now)[:7]

data=pd.read_csv("birthdays.csv")
df=pd.DataFrame(data)

birth_list=[]
for index,row in df.iterrows():

    birthdays={}
    birth_date=''
    birth_date+=str(row.year)
    birth_date+='-'
    if row.month<10:
        birth_date+='0'
        birth_date+=str(row.month)
    else:
        birth_date+=str(row.month)
    birthdays['birthday']=birth_date
    birthdays['name']=row['name']
    birth_list.append(birthdays)

for i in birth_list:
    if now==i['birthday']:
        letter_templates=['letter_1.txt','letter_2.txt','letter_3.txt']
        template_chosen=random.choice(letter_templates)
        with open('letter_templates/'+template_chosen) as letter:
            send=letter.read()
            send=send.replace('[NAME]',i['name'])
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(from_addr=email, to_addrs="vanshikasaxena0207@gmail.com",
                                    msg=f"Subject:Happy Birthday !{i['name']}\n\n {send}")






