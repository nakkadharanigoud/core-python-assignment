def calculate_fare(distance):
    """Calculate total fare for one trip."""
    base_fare = 50
    per_km_rate = 10
    return base_fare + (distance * per_km_rate)

def total_fare(trips):
    """Calculate total fare for all trips."""
    fares = [calculate_fare(d) for d in trips]
    total = sum(fares)
    return fares, total


if __name__ == "__main__":
    trips = [5, 10, 3]  # distances in km
    fares, total = total_fare(trips)

    for i, fare in enumerate(fares, start=1):
        print(f"Trip {i}: ${fare}")
    print(f"Total Fare: ${total}")
