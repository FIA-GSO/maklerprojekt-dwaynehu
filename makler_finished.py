# Input of room dimensions
total_size = 0
add_room = "y"
room_number = 1
all_rooms_dict= {}
## add eval(input)_input instead of input
while add_room == "y":
    #    room_number = room_number + 1
    # ERROR Handling: input validation for float
    while True:
        try:
            room_dim_a = float(input(f"Enter dimension a of room {room_number}:"))
            room_dim_b = float(input(f"Enter dimension b of room {room_number}:"))
            break
        except ValueError:
            print("Please use numbers. Try again!")
    # calculate room size and add room size to total_size
    room_size = room_dim_a * room_dim_b
    total_size = total_size + room_size
    room_name=input(f"give the room a name:")
    all_rooms_dict[room_name] = room_size
    obstruction = input("obstruction? (y/n)")
    if obstruction[0] == "y":
        while True:
            try:
                obstruction_dim_a = float(input("Please enter the dimension a for the obstruction: "))
                obstruction_dim_b = float(input("Please enter the dimension b for the obstruction: "))
                break
            except ValueError:
                print("Please use numbers. Try again!")
        obstruction_dim = obstruction_dim_a * obstruction_dim_b
        total_size = total_size + obstruction_dim
        add_room = input("Do you want to add more rooms? (y/n)")
        room_number = room_number + 1 # increase counter for room number
    # user chose no obstruction
    elif obstruction[0] == "n":
        add_room = input("Do you want to add more rooms? (y/n)")
        room_number = room_number + 1 # increase counter for room number
    else:  # Output if user did not type yes or no
        print("Type yes or no. Try again!")

print(f"Total room size is: {total_size} m2") # Output total room size
print("The average room size is: ", total_size/(room_number-1),"m2") # Output average room size
print("Summary:", all_rooms_dict)
