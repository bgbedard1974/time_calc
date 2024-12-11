class Time:
    def __init__(self, string = ''):
        if string == '':
            self.minutes = 0
        else:
            self.minutes = self.parse(string)

    # Add minutes from another Time object
    def add(self, time_obj):
        self.minutes = self.minutes + time_obj.minutes
    
    def parse(self, string):
        temp_minutes = 0
        parts = string.split(":")
        if parts[0] != '':
            temp_minutes = temp_minutes + int(parts[0]) * 60
        if parts[1] != '':
            temp_minutes = temp_minutes + int(parts[1])
        return temp_minutes

    def debug(self):
        print ("Minutes: " + str(self.minutes))

    def __str__(self):
        temp_hours = 0
        temp_minutes = self.minutes
        while temp_minutes > 60:
            temp_hours = temp_hours + 1
            temp_minutes = temp_minutes - 60

        zero = ''
        if temp_minutes < 10:
            zero = '0'
        output = "{}:{}{}".format(temp_hours,zero,temp_minutes)
        return output