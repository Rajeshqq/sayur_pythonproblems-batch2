theater = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]


def print_theater():
    for row in theater:
        for seat in row:
            print(seat, end='   ')
        print(" ")
        print(" ")


def book_seat(placement, nof_seat):
    start = 0
    end = 0
    count = nof_seat
    div = len(theater) // 3
    theater_row = theater
    no_of_seat_in_row = len(theater_row[0])
    your_booked_tick = []
    
    if placement == "bottom":
        start = 0
        end = div - 1
    elif placement == "middle":
        start = div
        end = start + div - 1
    else:
        start = div * 2
        end = start + div - 1 + (len(theater) % 3)

    if theater_row[end][no_of_seat_in_row - 1] != 'X':
        for i in range(start, end + 1):
            for j in range(no_of_seat_in_row):
                if theater_row[i][j] == 0:
                    theater_row[i][j] = "X"
                    seat_label = chr(65 + i) + str(j + 1)
                    your_booked_tick.append(seat_label)
                    count -= 1
                    if count <= 0:
                        break

            if count <= 0:
                break
    else:
        print(f"The seats are full for {placement} placement")

    return your_booked_tick


print_theater()

# User Input for booking seats
while True:
    placement_input = input("Enter placement (bottom, middle, top) or 'q' to quit: ")
    if placement_input.lower() == 'q':
        break
    no_of_seats_input = int(input("Enter number of seats: "))
    
    booked_seats = book_seat(placement_input.lower(), no_of_seats_input)
    print_theater()
    
    if booked_seats:
        print("Your booked seats:")
        for seat in booked_seats:
            print(seat, end=', ')
        print()

print("Thank you for booking!")
