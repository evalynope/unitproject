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

EVENTS_DIR = "events"
os.makedirs(EVENTS_DIR, exist_ok=True)

attendees = [] # list of 'Attendee' instances
events = [] # list of 'Event' instances

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

def login_with_username_password() -> bool: #RUSS #Lets you login and will deny your credentials if pw is incorrect.
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


def create_event_from_input() -> None: #action [1]
  
    event_dates = []
    date_format = "%m/%d/%Y"
    time_format = "%H:%S"
    name  = input("Event name: > ") 
    while True: 
        date = input("Enter the date (MM/DD/YYYY). > ")
        if date in event_dates:
            print("An event already exists on that date. Please choose another.")
        else:
            try:
                datetime.strptime(date, date_format)
                event_dates.append(date)
                date = Event.date # Russ
                break
            except ValueError: 
                print("Invalid Date Format. Please use full month name and numerical day of the month")
    while True:
        time = input("Event time (HH:MM) > ")
        try: 
            datetime.strptime(time, time_format)
            time = Event.time # Russ
            break
        except ValueError:
            print("Invalid time format. Please enter the hour, minute, and am or pm. (07:00 PM)")    
    while True:
        place = input("Place: > ")
        place = Event.place
        break
    name = Event(f"{name}", date, time, f"{place}")
    print(name)
    with open(f"{name}.txt", "w") as file:
        file.write(name)
        file.close
    event_dates.append(name)
    


def view_all_events(directory = EVENTS_DIR) -> list: #action [2] 
    if not os.path.exists(directory):
        print("No events folder found.")
        return
    files = [f for f in os.listdir(directory) if f.endswith(".txt")]
    if not files:
        print("No events found.")
    if files:
        for file in files:
            print(f"\n--- {file} ---\n") #not sure I love how this looks...to revisit later
            with open(os.path.join(directory, file), "r") as f:
                print(f.read())
                print("\n--------------")
                
def register_attendee(): 
    name = input("Name of attendee: ")
    phone = input("Phone number: ")
    event = input("Event to register for: ")
    attendees.append(name, phone, event)
    print(attendees)

    name = Attendee(f"{name}",f"{phone}", f"{event}")
    with open(f"{name}.txt", "w") as file:
        file.write(name)
        file.close

    return Attendee(name, phone, event)

   

    



def update(): #action [3]
    pass

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
                print("[1] Create an event \n[2] View all events \n[3] Register for an event \n[4] See events you’re registered for  \n[5] Cancel registration or event \n[6] Quit")
                action = input("> ")
                if action.strip() == '1':
                    event = create_event_from_input()
                    with open(os.path.join(EVENTS_DIR, f"{event.name}.txt"), "w") as file:
                    # (f"{event.name}.txt", "w") as file: ## This was what I used before I created an events folder. 
                        file.write(f"{event.name} \n{event.date} \n{event.time} \n{event.place}")
                        print(f"Event saved as {event.name}.txt in the events folder.") 
                elif action.strip() == '2': #VIEW EVENTS
                    print("Viewing all events")
                    view_all_events()    
                elif action.strip() == '3':
                    register_attendee()
                elif action.strip() == '4':
                    pass        
                elif action.strip() == '6':
                    print("Goodbye!")
                    break
  
            
        


    

if __name__ == '__main__':
    main()