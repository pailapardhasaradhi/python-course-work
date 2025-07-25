room_id = int(input("Enter Room ID: "))
room_type = input("Enter Room Type (Single/Double/Suite): ")
price_per_night = float(input("Enter Price per Night (₹): "))
facilities = input("Enter Facilities : ").split(",")
stock_info = (10, 5)  
discount = float(input("Enter Discount Percentage: "))
special_services = set(input("Enter Special Services : ").split(","))
hotel_info = {
    "Name": "Sunset Hotel",
    "Location": "Hyderabad",
    "Contact": "9876543210"
}

# Booking Details
guest_name = input("Enter Guest Name: ")
nights = int(input("Enter Number of Nights: "))

# Calculate Discounted Price and Total
discounted_price = price_per_night * (1 - discount / 100)
total_amount = discounted_price * nights

# --- Output using formatting methods ---

# sep=',' formatting
print("\nRoom ID, Type, Price:", room_id, room_type, price_per_night, sep=", ")

# % formatting
print("Discount: %.2f%%" % discount)

# f-string
print(f"Guest Name: {guest_name}")
print(f"Room Type: {room_type}")
print(f"Facilities: {', '.join(facilities)}")
print(f"Special Services: {', '.join(special_services)}")
print(f"Available Rooms: {stock_info[0]}, Booked Rooms: {stock_info[1]}")
print(f"Discounted Price per Night: ₹{discounted_price}")
print(f"Nights Stayed: {nights}")
print(f"Total Bill: ₹{total_amount}")

# .format() method
print("Hotel Details: Name - {0}, Location - {1}, Contact - {2}".format(
    hotel_info["Name"], hotel_info["Location"], hotel_info["Contact"]
))
