def adjust_light(level):
    if level == 0:
        print("Turning off the light.")
    elif level == 1:
        print("Setting light to Low (25%).")
    elif level == 2:
        print("Setting light to Medium (50%).")
    elif level == 3:
        print("Setting light to High (75%).")
    elif level == 4:
        print("Setting light to Maximum (100%).")
    else:
        print("Invalid input. Please enter a number between 0 and 4.")

def main():
    while True:  # This creates an infinite loop
        try:
            choice = int(input("Enter the desired level for the light (0-4): "))
            if 0 <= choice <= 4:
                adjust_light(choice)
                if choice == 0:  # If the choice is 0, break out of the loop
                    break
            else:
                print("Invalid input. Please enter a number between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
