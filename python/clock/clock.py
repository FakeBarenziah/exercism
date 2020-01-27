class Clock:
    def __init__(self, hour, minute):
        minute += (hour * 60)
        while minute < 0:
            minute += 1440
        self.hour = int(minute / 60) % 24
        self.minute = minute % 60

    def __repr__(self):
        string_hour = str(self.hour)
        string_minute = str(self.minute)
        
        if len(string_hour) < 2:
            string_hour = "0%s" % string_hour
        if len(string_minute) < 2:
            string_minute = "0%s" % string_minute
        
        clock = "%s:%s" %(string_hour, string_minute)
        return clock

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        total_minute = self.minute + (self.hour * 60) + minutes

        new_hour = int(total_minute / 60) % 24
        new_minute = total_minute % 60

        self = Clock(new_hour, new_minute)
        return self

    def __sub__(self, minutes):
        total_minute = self.minute + (self.hour * 60) - minutes

        while total_minute < 0:
            total_minute += 1440
        
        new_hour = int(total_minute / 60) % 24
        new_minute = total_minute % 60
        
        self = Clock(new_hour, new_minute)
        return self
