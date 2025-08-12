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

def get_username_password() -> NoReturn: #creates new user name and new password #RUSS
 while True:
        username = input("Username: > ").strip()
        file_path = f"{username}.txt"
        if os.path.exists(file_path):
            print("That username already exists.")
        else:
            with open(f"{username}.txt", "w") as new_user:
                password = input("Password: > ").strip()
                new_user.write(password)
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

    
    while True: 
        print("Welcome to Event Registration! \n[1] Login \n[2]Create a username and password.")
        login_input = input("> ")
        if login_input.strip() == "1":
            login_with_username_password() 
        elif login_input.strip() == "2":
            get_username_password()
        else: print("Not a valid choice. Please enter '1' to login or '2' to create a new username and password.")
        break

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

          # where 3-5 will go         
        elif action.strip() == '6':
            print("Goodbye!")
            break
        else: 
            print("Invalid entry. Please select from the following:^^ ")


        








    






if __name__ == '__main__':
    main()