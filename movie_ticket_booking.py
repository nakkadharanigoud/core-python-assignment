"""
Movie Ticket Booking System
---------------------------
Manages available and booked seats, with options to book or cancel.
"""

def available_seats(total_seats, booked):
    """Return list of available seats."""
    return [seat for seat in range(1, total_seats + 1) if seat not in booked]

def book_seat(booked, seat_num, total_seats):
    """Book a seat if available."""
    if seat_num in booked:
        print(f"Seat {seat_num} is already booked.")
    elif seat_num < 1 or seat_num > total_seats:
        print("Invalid seat number.")
    else:
        booked.append(seat_num)
        print(f"Seat {seat_num} booked successfully.")
    return booked

def cancel_seat(booked, seat_num):
    """Cancel a booked seat."""
    if seat_num in booked:
        booked.remove(seat_num)
        print(f"Seat {seat_num} cancelled successfully.")
    else:
        print(f"Seat {seat_num} was not booked.")
    return booked


if __name__ == "__main__":
    total_seats = 10
    booked_seats = [2, 5, 7]
    book_seat_num = 3
    cancel_seat_num = 5

    booked_seats = book_seat(booked_seats, book_seat_num, total_seats)
    booked_seats = cancel_seat(booked_seats, cancel_seat_num)

    print("Available seats:", available_seats(total_seats, booked_seats))
