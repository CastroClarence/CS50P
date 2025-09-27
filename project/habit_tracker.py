from habit import Habit
import sys
from datetime import date
import csv

# todo:
# Try to simplify check_duplicate
# Implement the habit streak reset function, return Valid, missed, done
class HabitTracker:
    FILE = "habits.csv"
    def __init__(self):
        self._habits = []
        self.load()
    def save(self):
        with open(self.FILE, "w") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "schedule", "streak", "date_marked", "date_created"])
            writer.writeheader()
            for habit in self._habits:
                writer.writerow(habit.to_dict())
    def load(self):
        try:
            print("Loading...")
            with open(self.FILE, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    habit = Habit(
                        name=row["name"],
                        streak=int(row["streak"]),
                        schedule=row["schedule"]
                    )
                    habit.date_created = date.fromisoformat(row["date_created"])
                    habit.date_marked = date.fromisoformat(row["date_marked"])
                    self._habits.append(habit)
        except FileNotFoundError:
            pass
    def check_duplicate(self, name: str):
        if len(self._habits) != 0:
            habits = [habit.name for habit in self._habits]
            if name in habits:
                return True
            return False
    def view_habits(self):
            """
            Returns a list of habits
            """
            if len(self._habits) > 0:
                return [habit for habit in self._habits]
            else:
                print("No habits yet.")
    def add_habit(self):
        """
        Adds a habit object to habits list
        """
        while True:
            habit = input("Habit: ")
            try:
                if not self.check_duplicate(habit):
                    print("Schedules are daily, weekly, monthly")
                    schedule = input("Schedule: ")
                    result = Habit(habit, schedule=schedule)
                    print(result.schedule)
                    self._habits.append(result)
                    action = input("Do you want to add another? Y/n\n : ")
                    if action == "Y":
                        continue
                    self.save()
                    return [habit.name for habit in self._habits]
                else:
                    return "Habit already exists."
            except AttributeError:
                # If schedule is invalid, try again
                continue
    def verify_completion(self, date_marked, schedule):
        """
        Verifies the date depending on its schedule
        Todo: This should accept the marked date, and its schedule(daily, weekly, monthly)
        - Return true or false
        """
        result =  date.today() - date_marked
        result = result.days
        if schedule == 'daily':
            if result > 0:
                return True
            else:
                print('test')
        elif schedule == 'weekly':
            if result > 7:
                return True
        elif schedule == 'monthly':
            if date.today().month - date_marked.month > 0 and result > 30:
                return True
        return False
    def mark_habit(self):
        """
        Marks a habit, indicating habit was done
        """
        habits = self._habits
        found = False
        if len(habits) == 0:
            print("No habits yet.")
            return None
        while True:
            print(*habits)
            name = input("Input habit: ")
            for habit in self._habits:
                if name == habit.name:
                    if self.verify_completion(habit.date_marked, habit.schedule):
                        habit.complete()
                        self.save()
                        print(f"{habit.name} in {habit.streak} streak/s. Keep it up!")
                    else:
                        print(f"{habit.schedule.capitalize()} Habit was already completed")
                    return None
            if found == False:
                print("Habit not found. Try again")
    def delete_habit(self):
        """
        Delete a habit based on given name.
        """
        habits = self._habits
        found = False
        while True:
            if len(habits) == 0:
                print("No habits yet.")
                return None
            print(*habits)
            name = input("Input habit: ")
            for habit in habits:
                if name == habit.name:
                    habits.remove(habit)
                    self.save()
                    print("Habit deleted.")
                    return None
            if not found:
                print("Habit not found.")
    def exit(self):
        """
        Terminates habit tracker
        """
        sys.exit("Continue improving!")
    def run(self):
        actions = {
            1 : ("Add habit" , self.add_habit),
            2 : ("View habits", self.view_habits),
            3 : ("Mark a habit", self.mark_habit),
            4 : ("Delete a habit", self.delete_habit),
            5 : ("Exit", self.exit)
        }
        while True:
            print("\n\n")
            for i, (name, _) in actions.items():
                print(f"{i}. {name}")
            try:
                action: int = int(input("Input number: "))
                if actions.get(action):
                    _, func = actions[action]
                    result = func()
                    print("\n")
                    if isinstance(result, list):
                        print("Habit/s: ", end="")
                        print(*result, sep=", ")
                    elif result is None:
                        continue
                    else:
                        print(result)
                else:
                    raise ValueError("Invalid input.")
            except Exception as e:
                sys.exit(f"Error: {e}")