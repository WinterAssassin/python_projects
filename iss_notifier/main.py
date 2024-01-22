import datetime
import time
import requests
import smtplib

ISS_URL = 'http://api.open-notify.org/iss-now.json#'
SS_URL = 'https://api.sunrise-sunset.org/json'

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
MY_LAT = 12.879721
MY_LONG = 121.774017


def is_iss_overhead():
    response = requests.get(ISS_URL)
    response.raise_for_status()

    data = response.json()

    iss_longitude = data['iss_position']['longitude']
    iss_latitude = data['iss_position']['latitude']

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        'lat': MY_LAT,
        'long': MY_LONG,
        'formatted': 0,
    }

    response = requests.get(SS_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = data['results']['sunset'].split('T')[1].split(':')[0]

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <=sunrise:
        return True
    

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )