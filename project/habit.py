from datetime import date
class Habit:
    """
    Habit class that have its name, schedule (daily or monthly or weekly)
    """
    def __init__(self, name: str, streak: int=0, schedule: str="daily"):
        schedules = ["daily", "weekly", "monthly"]
        self.name = name
        self._streak = streak
        self.date_created = date.today()
        self.date_marked = date.today()
        if schedule in schedules:
            self.schedule = schedule
        else:
            print("Invalid schedule. Try again")
    def __str__(self):
        return f"{self.name}"
    @property
    def streak(self):
        return self._streak
    @streak.setter
    def streak(self, streak):
        self._streak = streak
    def complete(self):
        self._streak += 1
        self.date_marked = date.today()
    def reset(self):
        self._streak = 0
    def to_dict(self) -> dict:
        return {
            "name" : self.name,
            "schedule" : self.schedule,
            "streak" : self.streak,
            "date_marked" : self.date_marked,
            "date_created" : self.date_created
        }