class Block:
    def __init(self, meeting_type=None,
               num=None, day_of_week=None,
               time=None, building=None,
               room=None, date=None):
        self.meeting_type = meeting_type
        self.num = num
        self.day_of_week = day_of_week
        self.time = time
        self.building = building
        self.room = room
        self.date = date
