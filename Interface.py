def menu():
     print ("1) Add appointment")
     print ("2) List appointment")
     print ("3) Cancel appointment") 
     print ("4) Exit")

def main():
     while True:
          menu()
          user_info = {}
          choice = input("Enter a number from 1-4 to select a feature: ").strip()

          # Work in progress, choices should have function with a dict
          if choice == "1":
               print("Add appointment function here\n")
               name = input("What is your name? ").strip()
               service = input("What service would you like? ").strip()
               date = input("What date would you like the appointment to be on? ")
               time = input("What time of day would like the appointment to be at? ")

          elif choice == "2":
               print("Add list appointment function here\n")
          
          elif choice == "3":
               print("Add cancel appointment function here\n")

          elif choice == "4":
               print("Add exit function here\n")
               break
          
          else: # Prints an error in case of incorrect input
               print("Please input an appropiate number 1-4 to control the menu\n")
               

if __name__ == "__main__":
    main()