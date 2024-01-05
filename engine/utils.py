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