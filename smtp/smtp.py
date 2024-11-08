import smtplib

# list of email_id to send the mail
li = ["aashimanker3007@gmail.com", "sivarathriamrutha@gmail.com","hellodear7931@gmail.com","akshithavanteddu@gmail.com"]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("thakurvidhatri45368@gmail.com", "App password ")
    message = "hello my dear friends"
    s.sendmail("thakurvidhatri45368@gmail.com", dest, message)
    s.quit()
