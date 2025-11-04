def book_ticket(booked, seat_no, total):
    if seat_no in booked:
        print("Seat", seat_no, "is already booked.")
    elif seat_no < 1 or seat_no > total:
        print("Invalid seat number.")
    else:
        booked.append(seat_no)
    return booked

def cancel_ticket(booked, seat_no):
    if seat_no in booked:
        booked.remove(seat_no)
    else:
        print("Seat", seat_no, "was not booked.")
    return booked

def available_seats(total, booked):
    seats = []
    for i in range(1, total + 1):
        if i not in booked:
            seats.append(i)
    return seats
total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5

booked_seats = book_ticket(booked_seats, book_seat, total_seats)
booked_seats = cancel_ticket(booked_seats, cancel_seat)

available = available_seats(total_seats, booked_seats)

print("Available seats:", available)
