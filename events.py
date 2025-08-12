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
    name  = input("Event name: ") 
    while True: 
        date = input("Enter the date (Month, day) ")
        while date in event_dates:
            print("An event already exists on that date. Please choose another.")
            date = input("Enter the date (Month, day) ")
        try:
            valid_date = datetime.strptime(date, "%B %d")
            break
        except ValueError: 
            if not valid_date:
                print("Invalid Date Format. Please use full month name and numerical day of the month")
        date = Event.date # Russ
    while True:
        time = input("Event time: ")
        try: 
            valid_time =  datetime.strptime(time, "%I:%M %p")
            break
        except ValueError:
            if not valid_time: 
                print("Invalid time format. Please enter the hour, minute, and am or pm. (07:00 PM)")    
    place = input("Place: ")   
    event_dates.append(date) # this  is a collection that can be looped through later for input validation    
    return Event(name, date, time, place)
    


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
                ### meat of the program goes here ###

    
                # while True: 
                #     login_create_input = input("Welcome to Event Registration! [L]ogin or [C]reate a username and password below.")
                #     if login_create_input.strip().lower() == "l":
                #         pass    
                #     elif login_create_input.strip().lower() == "c":
                #         pass
                #     else: print("Not a valid choice. Please enter 'L' to Login or 'C' to Create.")
                #     break

                while True: 
                    print("[1] Create an event \n[2] View all events \n[3] Update user info or event info \n[4] Quit")
                    action = input("> ")
                    if action.strip() == '1':
                        create_event_from_input()
                        save_event_in_txt_file(event)
                    # elif action.strip() == '2':
                    #     pass
                    # elif action.strip() == '3':
                    #     pass
                    elif action.strip() == '4':
                        print("Goodbye!")
                        break
                    else: 
                        print("Invalid entry. Please select from the following: [1] Create an event \n[2] View all events \n[3] Update user info or event info")

        else:
            print("Invalid entry.")


        








    






if __name__ == '__main__':
    main()