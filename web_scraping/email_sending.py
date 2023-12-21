from email.message import EmailMessage
import ssl
import smtplib
from web_scraping_online import * # for importing the func
from datetime import date, timedelta, datetime
import time


email_recepient = 'devin.wingfield45@gmail.com' #whos receiving
email_password = 'rwhfxothcdhekbam' # got from apppassword in google account
email_sender = 'devin.wingfield45@gmail.com'#whos sending

#contents of email | can change into email sent when info changes
subjet = 'results'
body = f"New reults of f1 race:\n(run code again to get another email)\n{print_result(length)}"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_recepient
em['Subject'] = subjet
em.set_content(body)

context = ssl.create_default_context()

today_date = date.today()
send_dates = []
for i in range(3,len(date_date) - 3,3): #imported from web_scraping_online
    race_date = date_date[i].text.split(" ")
    for j in range(0,len(race_date),2):
        month_num = month_to_num(race_date[j])
        race_date.remove(race_date[j]) 
        race_date.insert(j, month_num)
        send_dates.append(date(2023, race_date[0], int(race_date[1])))

sending_date = date(2023,1,1)
for send_date in send_dates:    
    if today_date - send_date < timedelta(0):
        sending_date = send_date
        break

def get_difference(date1, date2):
    delta = date2 - date1
    return delta.days

def days_to_seconds(days):
    seconds = (days+1) * 86400 #seconds in a day & adding a day since we dont know when the race will be
    return seconds

days = get_difference(today_date,sending_date)
seconds_sleep = days_to_seconds(days)
send_time = datetime.now().strftime('%H:%M:%S')
print("email will be sent the day after", sending_date, "at", send_time)
time.sleep(seconds_sleep)

# password and sending the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_recepient, em.as_string())

print("email has been sent")