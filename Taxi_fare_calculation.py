def calculate_fare(distance):
    base_fare = 50
    per_km = 10
    fare = base_fare + (distance * per_km)
    return fare

trips = [5, 10, 3]   # distance in km
total = 0

for i in range(len(trips)):
    trip_fare = calculate_fare(trips[i])
    print("Trip", i + 1, ":", "$" + str(trip_fare))
    total += trip_fare

print("Total Fare:", "$" + str(total))
