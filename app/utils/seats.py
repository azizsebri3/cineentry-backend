def generate_seats(capacity: int):
    if capacity <= 0:
        return []
    
    rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    seats = []
    count = 0

    for row in rows:
        for number in range(1, 21):  # max 20 seats per row
            seats.append(f"{row}{number}")
            count += 1
            if count == capacity:
                return seats
