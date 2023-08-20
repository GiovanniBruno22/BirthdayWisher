import smtplib

import pandas
from datetime import datetime
import random

MY_EMAIL = "YOUREMAILHERE"
MY_PASSWORD = "YOURPASSWORDHERE"

month = datetime.now().month
day = datetime.now().day
today = (month, day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if(month, day) in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="test@test.com",
                            msg=f"Subject:Happy Birthday\n\n{contents}")
