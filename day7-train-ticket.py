# day7-train-ticket.py


passenger_age = int(input("Enter passenger age: "))
base_fare = float(input("Enter base fare (e.g., 500): "))

tatkal_input = input("Is Tatkal? (yes/no): ").strip().lower()
is_tatkal = (tatkal_input == "yes")


if passenger_age < 5:
    final_fare = 0.0
elif 5 <= passenger_age <= 12:
    final_fare = base_fare * 50/100
elif passenger_age > 60:
    final_fare = base_fare * 60/100
else:
    final_fare = base_fare

if is_tatkal:
    final_fare = final_fare * 1.30


print(f"Ticket Confirmed | Age: {passenger_age} | Fare: Rs. {final_fare}")