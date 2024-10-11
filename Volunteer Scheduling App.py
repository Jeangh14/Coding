from collections import deque

sign_up_stack = []

volunteer_queue = deque()

available_opportunities = []

def sign_up(volunteer):
    sign_up_stack.append(volunteer)
    volunteer_queue.append(volunteer)
    print(f"{volunteer} has signed up.")

def undo_sign_up():
    if sign_up_stack:
        last_volunteer = sign_up_stack.pop()
        volunteer_queue.remove(last_volunteer)
        print(f"Undo: {last_volunteer}'s sign-up has been undone.")
    else:
        print("No sign-ups to undo.")

def schedule_next():
    if volunteer_queue:
        next_volunteer = volunteer_queue.popleft()
        print(f"{next_volunteer} has been scheduled for an opportunity.")
    else:
        print("No volunteers to schedule.")

def add_opportunity(opportunity):
    available_opportunities.append(opportunity)
    print(f"Opportunity '{opportunity}' has been added.")
    
def fill_opportunity(opportunity):
    if opportunity in available_opportunities:
        available_opportunities.remove(opportunity)
        print(f"Opportunity '{opportunity}' has been filled.")
    else:
        print(f"Opportunity '{opportunity}' not found.")

if __name__ == "__main__":
    add_opportunity("Food Bank Shift")
    add_opportunity("Park Clean-up")
    
    sign_up("Alice")
    sign_up("Bob")
    
    schedule_next()
    
    undo_sign_up()
    
    schedule_next()

    fill_opportunity("Food Bank Shift")
