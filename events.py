
from dataclasses import dataclass
from datetime import datetime
from typing import NoReturn
import os

@dataclass
class Attendee():
    name: str
    phone: int
    event: str

@dataclass
class Event():
    name: str 
    date: datetime
    time: datetime
    place: str

class Event:
    def __init__(self, name, date, time, place):
        self.name = name
        self.date = date
        self.time = time
        self.place = place

    def __str__(self):
        return f"Event: {self.name}\nDate: {self.date}\nTime: {self.time}\nVenue: {self.place}"

EVENTS_DIR = "events" #folder
os.makedirs(EVENTS_DIR, exist_ok=True)

ATTENDEES_DIR = "attendees" 
os.makedirs(ATTENDEES_DIR, exist_ok=True)

attendees = [] 
event_dates = [] 
events = []

def get_username_password() -> NoReturn:
    while True:
        username = input("Username: > ").strip()
        file_path = f"{username}.txt"
        if os.path.exists(file_path):
            print("That username already exists.")
        else:
            print(f"Username created: {username}")
            with open(f"{username}.txt", "w") as new_user:
                password = input("Password: > ").strip()
                new_user.write(password)
                print("Password saved.")
                new_user.close
                break

def login_with_username_password() -> bool: #RUSS 
    while True:
        username = input("Username: > ").strip()
        try:
            while True:
                with open(f"{username}.txt", "r") as checker:
                    stored_password = checker.readline().strip()
                    password = input("Password: > ").strip()
                    if password == stored_password:
                        return True
                    else:
                        print("Invalid login credentials.")
        except FileNotFoundError:
            print("Invalid login credentials.")

#### Russ create and view event below ####
def create_event(existing_datetimes: list[datetime] = None) -> Event:
    date_format = "%m/%d/%Y"
    time_format = "%H:%M"
    event_name = input("Event name: > ").strip()

    while True:
        file_path = f"{event_name}.txt"
        if os.path.exists(file_path):
            print("That event name has already been taken.")
        else:
            while True:
                event_date = ""
                event_time = ""
                while True:
                    try:
                        event_date_str = input("Date (MM/DD/YYYY): > ").strip()
                        event_date = datetime.strptime(event_date_str, date_format).date()
                        break
                    except ValueError:
                        print("Invalid date.")
                while True:
                    try:
                        event_time_str = input("Time (HH:MM): > ").strip()
                        event_time = datetime.strptime(event_time_str, time_format).time()
                        break
                    except ValueError:
                        print("Invalid time.")

                combined_datetime = datetime.combine(event_date, event_time)
                print(f"{combined_datetime} - {existing_datetimes}")
                if combined_datetime in existing_datetimes:
                    print(f"{event_time_str} on {event_date_str} is already taken.\nPlease choose another date and time.")
                else:
            
                    event_venue = input("Venue: > ").strip()
                    event = Event(event_name, event_date, event_time, event_venue)
                    print(event)
                    with open(file_path, "w") as file:
                        file.write(f"{event_date}\n")
                        file.write(f"{event_time}\n")
                        file.write(f"{event_venue}\n")
                        print("Event saved successfully.")
                        existing_datetimes.append(combined_datetime)
                        print(existing_datetimes)
                        return event 
        event_name = input("Event name: > ").strip()
           

def view_event():
    search_name = input("Search by event name: > ")
    file_path = f"{search_name}.txt"
    try:
        with open(f"{file_path}.txt", "r") as file:
            lines = file.readlines()
            date, time, location = [line.strip() for line in lines]
            print("-------------------")
            print(f"{search_name}")
            print(f"{date}")
            print(f"{time}")
            print(f"{location}")
            print("-------------------")
    except FileNotFoundError:
        print("Not found.")
#### Russ create event and view above

def view_all_events(directory = EVENTS_DIR) -> None: 
    if not os.path.exists(directory):
        print("No events folder found.")
        return
    files = [f for f in os.listdir(directory) if f.endswith(".txt")]
    if not files:
        print("No events found.")
    if files:
        for file in files:
            print(f"\n--- {file} ---\n") 
            with open(os.path.join(directory, file), "r") as f:
                print(f.read())
                print("\n--------------")



def view_all_events(directory = EVENTS_DIR) -> None: 
    if not os.path.exists(directory):
        print("No events folder found.")
        return
    files = [f for f in os.listdir(directory) if f.endswith(".txt")]
    if not files:
        print("No events found.")
    if files:
        for file in files:
            print(f"\n--- {file} ---\n") 
            with open(os.path.join(directory, file), "r") as f:
                print(f.read())
                print("\n--------------")



def view_all_events(directory = EVENTS_DIR) -> None: 
    if not os.path.exists(directory):
        print("No events folder found.")
        return
    files = [f for f in os.listdir(directory) if f.endswith(".txt")]
    if not files:
        print("No events found.")
    if files:
        for file in files:
            print(f"\n--- {file} ---\n") 
            with open(os.path.join(directory, file), "r") as f:
                print(f.read())
                print("\n--------------")


 

def get_all_events() -> list[Event]:
    events = []
    for filename in os.listdir(EVENTS_DIR):
        if filename.endswith(".txt"):
            with open(os.path.join(EVENTS_DIR, filename), "r") as file:
                lines = file.read().strip().split("\n")
                if len(lines) >= 4:
                    name, date, time, place = lines[:4]
                    events.append(Event(name, date, time, place))
    return events

 
def get_phone():
    while True:
        phone = input("10-digit phone number: ")
        if not phone.isdigit() or len(phone) != 10:
            print("Invalid number.")
        else:
            return phone

def register_attendee() -> Attendee: 
                
    events = get_all_events()
    if not events: 
        print("No events to register for.")
        return
    print("Available events:")

    lowered_events = []
    for e in events: 
        print(f"- {e.name}")
        lowered_events.append(e.name.lower().strip())


    event = input("Event to register for: ").strip().title()

    attendeeToReturn = None
    for e in events:
        while attendeeToReturn == None:
            if e.name.lower().strip() == event.lower().strip():
                name = input("Name: ").strip().title()
                phone = get_phone()
                attendee = Attendee(name, phone, event)
                attendees.append(attendee)
                for a in attendees: 
                    print(f"{a.name} is registered for the {a.event}!")
                name = Attendee(f"{name}",f"{phone}", f"{event}")
                filename = os.path.join(ATTENDEES_DIR, f"{attendee.name}.txt")
                with open(filename, "a") as file:   
                    file.write(f"{attendee.name} | {attendee.phone} | {attendee.event}\n")
                    file.close
                attendeeToReturn = attendee
                break
            elif event.lower().strip() in lowered_events:
                break
            else:
                print("event doesn't exist")
                event = input("Event to register for: ").strip().title()

    return attendeeToReturn
                       
            
def see_events_registered_for() -> None:
    name_search = input("Name to search for: ").strip().lower()
    found_events = []

    for filename in os.listdir(ATTENDEES_DIR):
        if filename.endswith(".txt"):
            with open(os.path.join(ATTENDEES_DIR, filename), "r") as file:
                for line in file:
                    items = line.strip().split("|")
                    if len(items) >= 3:
                        name, phone, event = [i.strip() for i in items]
                        if name.lower() == name_search:
                            found_events.append(event)

    if found_events:
        print(f"{name_search.title()} is registered for:")
        for event in found_events:
            print(f"- {event}")
    else:
        print(f"No events found for {name_search.title()}.")

def update_event():
    while True: # keeping inside the funct
        event = input("Enter the name of the event to update: > ")
        path = f"events/{event}.txt"

        if not os.path.exists(path):
            print("Not found.")
            # return
        ### updates below ###
        else:
            with open(path, "r") as file:
                lines = file.readlines()
                current_name = lines[0].strip()
                current_date = lines[1].strip()
                current_time = lines[2].strip()
                current_place = lines[3].strip()

            new_name = input(f"New name (current: {current_name}): > ")
            if not new_name:
                new_name = current_name

            new_date = input(f"New date (current: {current_date}): > ")
            if not new_date:
                new_date = current_date

            new_time = input(f"New time (current: {current_time}): > ")
            if not new_time:
                new_time = current_time

            new_place = input(f"New place (current: {current_place}): > ")
            if not new_place:
                new_place = current_place

            if new_name != current_name:
                os.remove(path) # trying to delete prev file
                new_path = f"events/{new_name}.txt"
                with open(new_path, "w") as file:
                    file.write(f"{new_name}\n{new_date}\n{new_time}\n{new_place}")

            else:
                with open(path, "w") as file:
                    file.write(f"{new_name}\n{new_date}\n{new_time}\n{new_place}")
            break
import os

def delete_event():
    current_name = input("Enter the name of the event to delete : > ")
    "events/<class '__main__.Event'>.txt"
    path = f"events/{current_name}.txt"
    while True: # keeping in funct
        if not os.path.exists(path):
            print("Not found.")
#            return
        else:
            os.remove(path)
            print(f"{current_name} deleted successfully.")
            break
        
#    with open(path, "r") as file:
#        lines = file.readlines()
#    current_name = lines[0].strip()
#    current_date = lines[1].strip()
#    current_time = lines[2].strip()
#    current_place = lines[3].strip()
#
#    new_name = input(f"New name (current: {current_name}): > ")
#    if not new_name:
#        new_name = current_name
#    
#    new_date = input(f"New date (current: {current_date}): > ")
#    if not new_date:
#        new_date = current_date
#    
#    new_time = input(f"New time (current: {current_time}): > ")
#    if not new_time:
#        new_time = current_time
#    
#    new_place = input(f"New place (current: {current_place}): > ")
#    if not new_place:
#        new_place = current_place
#    
#    if new_name != current_name:
#        new_path = f"events/{new_name}.txt"
#        with open(new_path, "w") as file:
#            file.write(f"{new_name}\n{new_date}\n{new_time}\n{new_place}")
#       
#    else:
#        with open(path, "w") as file:
#            file.write(f"{new_name}\n{new_date}\n{new_time}\n{new_place}")
    
   

def main():

    print("Welcome to our event registration page!")
    existing_datetimes = []
    while True:
        action = input("[1] New user\n[2] Login\n[3] Exit\n> ").strip()
        if action == "3":
            break
        elif action == "1":
            get_username_password()
        elif action == "2":
            unlock = login_with_username_password()
            if unlock == True:
                while True: 
                    print("[1] Create an event \n[2] View all events \n[3] Register for an event \n[4] See events you’re registered for  \n[5] Update event's information \n[6] Delete an event \n[7] Log Out")
                    action = input("> ")
                    if action.strip() == '1':
                        event = create_event(existing_datetimes)
                        with open(os.path.join(EVENTS_DIR, f"{event.name}.txt"), "w") as file:
                            file.write(f"{event.name} \n{event.date} \n{event.time} \n{event.place}")
                            print(f"Event saved as {event.name}.txt in the events folder.") 
                    elif action.strip() == '2': 
                        print("Viewing all events")
                        view_all_events()
                    elif action.strip() == '3':
                        register_attendee()
                    elif action.strip() == '4':
                        see_events_registered_for() 
                    elif action.strip() == '5':
                        update_event()
                    elif action.strip() == '6':
                        delete_event()             
                    elif action.strip() == '7':
                        print("Goodbye!")
                        break
        else:
            print("Invalid entry.")
   
if __name__ == '__main__':
    main()
      



        




