from twilio.rest import Client
import constants
import os
from dotenv import load_dotenv

class Time:
    def __init__(self, hour: int, minute: int):
        self.hour = abs(hour) % 24
        self.minute = abs(minute) % 60
    
    def __str__(self):
        f_hour = str(self.hour).zfill(2)
        f_min = str(self.minute).zfill(2)
        return f"{f_hour}:{f_min}"
    
    def __repr__(self):
        f_hour = str(self.hour).zfill(2)
        f_min = str(self.minute).zfill(2)
        return f"{f_hour}:{f_min}"
    
    def __add__(self, other):
        return Time(self.hour + other.hour, self.minute + other.minute)
    

# GET RID OF THIS AND JUST REPLACE WITH YOUR OWN (OR MAKE .env FILE)
def get_sms_api():
    load_dotenv()
    return os.getenv["TWILIO_SID"], os.getenv["TWILIO_AUTH"], os.getenv["TWILIO_NUM"], os.getenv["TARGET_NUM"]

def send_text(text, playlist):
    sid, auth, twilio_num, target_num = get_sms_api() 
    client = Client(sid, auth)
    msg = client.messages.create(
        body=f"\n{text.strip('"')} \n\nPS. Listen to this: {playlist} \n:)",
        from_=twilio_num,
        to=target_num
    )

    # TODO: make it just launch spotify instead of sending playlist link