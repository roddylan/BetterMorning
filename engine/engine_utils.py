from twilio.rest import Client
import os
from dotenv import load_dotenv
from collections import defaultdict
import cv2
import numpy as np

class Time:
    def __init__(self, hour: int, minute: int):
        self.minute = abs(minute) % 60
        extra = abs(minute) // 60
        self.hour = abs(hour) % 24 + extra
    
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
    
    def __sub__(self, other):
        return Time(self.hour - other.hour, self.minute - other.minute)

class Schedule:
    def __init__(self, events: dict):
        self.events = events
        '''
        {
            "name": "desc"
            ...
        }        
        '''
        self._schedules = defaultdict(list)
    
    def get_schedules(self):
        return self._schedules
    
    def get_schedule(self, label):
        keys = self._schedules.keys()
        if label in set(keys):
            return self._schedules[label]
        else:
            return self._schedules[list(keys)[0]]
        
    def get_events(self):
        return self.events
    
    def make_schedule(self, label, events: list):
        # self._schedules[label] = []
        for event in events:
            self._schedules[label].append(self.events[event])


class WorkoutPlan:
    def __init__(self):
        # TODO: FINISH
        pass


# GET RID OF THIS AND JUST REPLACE WITH YOUR OWN (OR MAKE .env FILE)
def get_sms_api():
    load_dotenv()
    return os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"), os.getenv("TWILIO_NUM"), os.getenv("TARGET_NUM")

def send_text(text, playlist):
    sid, auth, twilio_num, target_num = get_sms_api() 
    client = Client(sid, auth)
    txt = text.strip('"')
    msg = client.messages.create(
        body=f"\n{txt} \n\nPS. Listen to this: {playlist} \n:)",
        from_=twilio_num,
        to=target_num
    )

    # TODO: make it just launch spotify instead of sending playlist link


def get_picture():
    cam = cv2.VideoCapture(0)
    result, img = cam.read()

    if result:
        return img
    return np.array(False)