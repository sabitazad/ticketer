class Ticket:
    ticket_count = 1

    def __init__(self, name, title, description, priority):
        self.ticket_id = Ticket.ticket_count
        self.name = name
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Open"
        Ticket.ticket_count += 1


class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, name, title, description):
        ticket = Ticket(name, title, description, "Normal")
        self.tickets.append(ticket)
        return ticket.ticket_id

    def get_ticket_by_id(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def update_ticket_status(self, ticket_id, new_status):
        ticket = self.get_ticket_by_id(ticket_id)
        if ticket:
            ticket.status = new_status
        else:
            print("Ticket not found.")

    def display_tickets(self):
        for ticket in self.tickets:
            print(f"Ticket ID: {ticket.ticket_id}")
            print(f"Name: {ticket.name}")
            print(f"Title: {ticket.title}")
            print(f"Description: {ticket.description}")
            print(f"Priority: {ticket.priority}")
            print(f"Status: {ticket.status}")
            print("------------------------------")

    def check_ticket_updates(self, ticket_id):
        ticket = self.get_ticket_by_id(ticket_id)
        if ticket:
            print(f"Ticket ID: {ticket.ticket_id}")
            print(f"Name: {ticket.name}")
            print(f"Title: {ticket.title}")
            print(f"Status: {ticket.status}")
        else:
            print("Ticket not found.")

    def run_user_end(self):
        while True:
            print("Ticketing System (User-End)")
            print("1. Create a new ticket")
            print("2. Check ticket updates")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter your name: ")
                title = input("Enter ticket title: ")
                description = input("Enter ticket description: ")
                ticket_id = self.create_ticket(name, title, description)
                print(f"Ticket created successfully! Ticket ID: {ticket_id}")
            elif choice == "2":
                ticket_id = int(input("Enter ticket ID: "))
                self.check_ticket_updates(ticket_id)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def run_admin_end(self):
        while True:
            print("Ticketing System (Admin-End)")
            print("1. Update ticket status")
            print("2. Display all tickets")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                ticket_id = int(input("Enter ticket ID: "))
                new_status = input("Enter new status: ")
                self.update_ticket_status(ticket_id, new_status)
                print("Ticket status updated successfully!")
            elif choice == "2":
                self.display_tickets()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def login(self):
        while True:
            print("Ticketing System (Login)")
            print("1. User login")
            print("2. Admin login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.run_user_end()
            elif choice == "2":
                password = input("Enter admin password: ")
                if password == "123":
                    self.run_admin_end()
                else:
                    print("Invalid password. Please try again.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

ticketing_system = TicketingSystem()
ticketing_system.login()
