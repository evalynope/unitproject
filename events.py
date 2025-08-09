from dataclasses import dataclass
from datetime import datetime

# trying to push

@dataclass
class Attendee():
    name: str
    phone: int
    event: str

class Event():
    name: str
    date: datetime
    time: datetime
    place: str

def read_events():
    pass

def create_event_from_input(): #action [1]
    name  = input("Event name: ") 
    while True: 
        date = input("Enter the date (Month, day) ")
        try:
            valid_date = datetime.strptime(date, "%B %d")
            break
        except ValueError: 
            print("Invalid Date Format. Please use full month name and numerical day of the month")
    while True:
        time = input("Enter event time as ")
        try: 
            valid_time =  datetime.strptime(time, "%I:%M %p")
            break
        except ValueError: 
            print("Invalid time format. Please enter the hour, minute, and am or pm. (07:00 PM)")    
    place = input("Place: ")       
    return Event(name, date, time, place)


with open(f"{event.name}.txt", "w") as file:
    file.write(f"{event.name} \n{event.date} \n{event.time} \n{event.place}")
    print(f"Event saved as {event.name}.txt")
    


def view_events(): #action [2]
    pass

def update(): #action [3]
    pass

def main():

    
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


        








    






if __name__ == '__main__':
    main()