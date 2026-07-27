from datetime import datetime
def menu():
     print ("1) Add appointment")
     print ("2) List appointment")
     print ("3) Cancel appointment") 
     print ("4) Exit\n")

def main():
     app_info = []
     appID = 0
     while True:
          menu()
          
          choice = input("Enter a number from 1-4 to select a feature: \n").strip()

          # Add a dictionary to a list with the relevant information
          if choice == "1":
               user_info = {}
               appID += 1
               
               while True: # Ensures that the name field cannot be empty
                    name = input("What is your name? ").strip()
                    if name:
                         break
                    print("Name cannot be empty. Please enter your name.")

               service = input("What service would you like? ").strip()

               while True:
                    date = input("What date would you like the appointment to be on? Please use YYYY-MM-DD format. ").strip()

                    try:
                         datetime.strptime(date, "%Y-%m-%d")
                         break  # Valid date
                    except ValueError:
                         print("Invalid date. Please use YYYY-MM-DD (example: 2026-08-31).")

               time = input("What time of day would like the appointment to be at? ").strip()

               appKey = "Appointment ID"
               nameKey = "Name"
               serviceKey = "Service"
               dateKey = "Date"
               timeKey = "Time"

               user_info[appKey] = appID
               user_info[nameKey] = name
               user_info[serviceKey] = service
               user_info[dateKey] = date
               user_info[timeKey] = time

               app_info.append(user_info)
               print()
               print(user_info)
               print()

          elif choice == "2":
               if not app_info:
                    print("\nThere are no appointments to display.\n")
               else:
                    print("\nViewing Appointments:")
                    print(f"\n{app_info}\n")
               
          
          elif choice == "3":

               while True: #Loops request until a valid input is inputted
                    cancelID = int(input("Enter the appointment ID to cancel: "))

                    if any(user["Appointment ID"] == cancelID for user in app_info): # Checks for user inputted appointment ID to ensure it exists before attempting to delete it
                         app_info = [user for user in app_info if user["Appointment ID"] != cancelID]
                         print(f"Appointment {cancelID} removed.")
                         break
                    else:
                         print("That appointment ID does not exist.")

          elif choice == "4":
               print("\nClosing program.\n")
               break
          
          else: # Prints an error in case of incorrect input
               print("Please input an appropiate number 1-4 to control the menu\n")
               

if __name__ == "__main__":
    main()