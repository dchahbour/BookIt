from datetime import datetime
import json
import os
import requests

def menu():
     print ("1) Add appointment")
     print ("2) List appointment")
     print ("3) Cancel appointment") 
     print ("4) Exit\n")

def main():

    manager = BookingManager()

    while True:

        menu()

        choice = input("Enter a number from 1-4 to select a feature: ").strip()

        if choice == "1":
            manager.add()

        elif choice == "2":
            manager.list()

        elif choice == "3":
            manager.cancel()

        elif choice == "4":
            print("\nClosing program.\n")
            break

        else:
            print("Please input a number from 1-4.\n")

class Service():
     def __init__(self, name: str, duration: int, price: float ):
          self.name = name
          self.duration = duration
          self.price = price

class Appointment:
    def __init__(self, appointment_id, name, service, date, time):
        self.appointment_id = appointment_id
        self.name = name
        self.service = service
        self.date = date
        self.time = time

    def to_dict(self):
        return {
            "Appointment ID": self.appointment_id,
            "Name": self.name,
            "Service": self.service,
            "Date": self.date,
            "Time": self.time
        }

    @staticmethod
    def from_dict(data):
        return Appointment(
            data["Appointment ID"],
            data["Name"],
            data["Service"],
            data["Date"],
            data["Time"]
        )

class BookingManager:

    FILE_NAME = "appointments.json"

    def __init__(self):

        self.services = [
            Service("Haircut", 30, 25.00),
            Service("Dentist", 60, 70.00),
            Service("Eye Exam", 45, 55.00),
            Service("Manicure", 30, 35.00)
        ]

        self.appointments = []
        self.appID = 0

        self.load()

    def load(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)

            for item in data:
                appointment = Appointment.from_dict(item)
                self.appointments.append(appointment)

            if self.appointments:
                self.appID = max(a.appointment_id for a in self.appointments)

    def save(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump(
                [a.to_dict() for a in self.appointments],
                file,
                indent=4
            )

    def check_holiday(self, date):

        year = date[:4]

        try:
            url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/US"
            holidays = requests.get(url, timeout=5).json()

            for holiday in holidays:
                if holiday["date"] == date:
                    print(f"\nWARNING: {date} is {holiday['localName']}.")
                    print("You may want to choose another day.\n")
                    break

        except requests.RequestException:
            print("Could not check holidays.")

    def add(self):

        while True:
            name = input("What is your name? ").strip()
            if name:
                break
            print("Name cannot be empty.")

        print("\nAvailable Services")

        for i, service in enumerate(self.services, start=1):
            print(f"{i}) {service.name} ({service.duration} min) - ${service.price:.2f}")

        while True:
            try:
                choice = int(input("Select a service: "))
                if 1 <= choice <= len(self.services):
                    break
            except ValueError:
                pass

            print("Invalid selection.")

        service = self.services[choice - 1]

        while True:
            date = input("Appointment date (YYYY-MM-DD): ").strip()

            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date.")

        self.check_holiday(date)

        time = input("Appointment time: ").strip()

        self.appID += 1

        appointment = Appointment(
            self.appID,
            name,
            service.name,
            date,
            time
        )

        self.appointments.append(appointment)
        self.save()

        print("\nAppointment booked!\n")

    def list(self):

        if not self.appointments:
            print("\nThere are no appointments.\n")
            return

        print()

        for appointment in self.appointments:
            print(appointment.to_dict())

        print()

    def cancel(self):

        if not self.appointments:
            print("\nThere are no appointments.\n")
            return

        while True:

            try:
                cancelID = int(input("Enter the appointment ID to cancel: "))
            except ValueError:
                print("Please enter a number.")
                continue

            for appointment in self.appointments:

                if appointment.appointment_id == cancelID:
                    self.appointments.remove(appointment)
                    self.save()
                    print(f"Appointment {cancelID} removed.")
                    return

            print("That appointment ID does not exist.")

if __name__ == "__main__":
    main()