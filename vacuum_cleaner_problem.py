# Vacuum Cleaner Problem with User Input

# Taking input from user
room_A = input("Enter status of Room A (Clean/Dirty): ")
room_B = input("Enter status of Room B (Clean/Dirty): ")

rooms = {"A": room_A, "B": room_B}

current_location = "A"

print("\nInitial State:", rooms)

while True:

    if rooms[current_location] == "Dirty":
        print("Room", current_location, "is Dirty. Cleaning...")
        rooms[current_location] = "Clean"
    else:
        print("Room", current_location, "is already Clean.")

    # Move to next room
    if current_location == "A":
        current_location = "B"
    else:
        current_location = "A"

    # Check if both rooms are clean
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nBoth rooms are clean. Task completed.")
        break

print("Final State:", rooms)
