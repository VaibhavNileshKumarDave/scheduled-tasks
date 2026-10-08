##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
PORT = 587

def send_birthday_wish_mail(receiver_email, letter_wishes):

    # connection = smtplib.SMTP("smtp.gmail.com")

    with smtplib.SMTP("smtp.gmail.com", port=PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=receiver_email, msg=f"Subject:HAPPY BIRTHDAY\n\n{letter_wishes}")

    # connection.close()

# 1. Update the birthdays.csv
birthdays_data = pd.read_csv("birthdays.csv")
birthdays_list = birthdays_data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

for birthday in birthdays_list:
    if birthday["month"] == now.month and birthday["day"] == now.day:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
        current_letter = random.choice(letters)

        with open(file=current_letter, mode="r") as letter_file:
            letter_content = letter_file.read()

        latest_letter = letter_content.replace("[NAME]", birthday["name"])

        with open(file="letter_templates/letter_main.txt", mode="w") as main_file:
            main_file.write(latest_letter)

# 4. Send the letter generated in step 3 to that person's email address.
        send_birthday_wish_mail(receiver_email=birthday["email"], letter_wishes=latest_letter)
