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

EVENTS_DIR = "events" #folder
os.makedirs(EVENTS_DIR, exist_ok=True)

ATTENDEES_DIR = "attendees" #folder 
os.makedirs(ATTENDEES_DIR, exist_ok=True)

attendees = [] # list of 'Attendee' instances
events = [] # list of 'Event' instances
event_dates = [] #list of dates taken by events

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
def create_event() -> Event:
    date_format = "%m/%d/%Y"
    time_format = "%H:%M"
    event_name = input("Event name: > ")
    event_date_time_list = []
    while True:
        file_path = f"{event_name}.txt"
        if os.path.exists(file_path):
            print("That event name has already been taken.")
        else:
            while True:
                event_date = input("Date (MM/DD/YYYY): > ")
                datetime.strptime(event_date, date_format)
                event_time = input("Time (HH:MM): > ")
                datetime.strptime(event_time, time_format)
                for combined_datetime in event_date_time_list:
                    combined_datetime = datetime.combine(event_date, event_time)
                    if combined_datetime in event_date_time_list:
                        print(f"{event_time} on {event_date} is already taken.\nPlease choose another date and time.")
                    else:
                        event_date_time_list.append(combined_datetime)
                event_venue = input("Venue: > ")
                event = Event(event_name, event_date, event_time, event_venue)
                print(event)
                with open(file_path, "w") as file:
                    file.write(f"{event_date}\n")
                    file.close
                with open(file_path, "a") as file:
                    file.write(f"{event_time}\n")
                    file.write(f"{event_venue}\n")
                    print("Event saved successfully.")
                    return event 
                    break
        break


###Evalyn get_all_events, register_attendee and see__events 

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
               
def register_attendee(): 

    events = get_all_events()
    if not events: 
        print("No events to register for.")
        return
    print("Available events:")
    for e in events: 
        print(f"- {e.name}")
    event = input("Event to register for: ").strip().title()
    name = input("Name: ").strip().title()
    phone = input("Phone: ").strip().title()
    attendee = Attendee(name, phone, event)
    attendees.append(attendee)
    for a in attendees: 
        print(f"{a.name} is registered for the {a.event}!")
    name = Attendee(f"{name}",f"{phone}", f"{event}")
    filename = os.path.join(ATTENDEES_DIR, f"{attendee.name}.txt")
    with open(filename, "a") as file:   
        file.write(f"{attendee.name} | {attendee.phone} | {attendee.event}\n")
        file.close
    return attendee

def see_events_registered_for():
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


def main():

    print("Welcome to our event registration page!")
    while True:
        action = input("1 - New user\n2 - Login\n3 - Exit\n> ").strip()
        if action == "3":
            break
        elif action == "1":
            get_username_password()
        elif action == "2":
            unlock = login_with_username_password()
            if unlock == True:
                while True: 
                    print("[1] -Create an event \n[2] -View all events \n[3] -Register for an event \n[4] -See events you’re registered for  \n[5] -Cancel registration or event \n[6] -Quit")
                    action = input("> ")
                    if action.strip() == '1':
                        event = create_event()
                        with open(os.path.join(EVENTS_DIR, f"{event.name}.txt"), "w") as file:
                            file.write(f"{event.name} \n{event.date} \n{event.time} \n{event.place}")
                            print(f"Event saved as {event.name}.txt in the events folder.") 
                    elif action.strip() == '2': 
                        print("Viewing all events")
                        get_all_events()    
                    elif action.strip() == '3':
                        register_attendee()
                    elif action.strip() == '4':
                        see_events_registered_for()       
                    elif action.strip() == '6':
                        print("Goodbye!")
                        break
        else:
            print("Invalid entry.")


        








    




    
if __name__ == '__main__':
    main()