import time
import pytesseract
import pyautogui
from PIL import Image
import smtplib
import sys

time.sleep(5)

screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')

text = pytesseract.image_to_string(Image.open('screenshot.png'))
print(text)

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

EMAIL = "EMAIL@gmail.com"  
PASSWORD = "PASSWORD" 

def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(auth[0], auth[1])
        server.sendmail(auth[0], recipient, message)  
        print(f"Message sent to {phone_number}@{carrier}")
        server.quit()
    except Exception as e:
        print(f"Failed to send message: {e}")

if __name__ == "__main__":
    while True:
        time.sleep(5)

        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        text = pytesseract.image_to_string(Image.open('screenshot.png'))
        print(text)
        if len(sys.argv) < 4:
            print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
            sys.exit(1)
        phone_number = sys.argv[1]
        carrier = sys.argv[2].lower()
        message = sys.argv[3]

        if carrier in CARRIERS:
            send_message(phone_number, carrier, message)
        else:
            print(f"Carrier '{carrier}' not found. Please use one of: {', '.join(CARRIERS.keys())}")