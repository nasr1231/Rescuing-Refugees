import math

# Set capacity of airplane
capacity = 350

num_refugees = int(input("How many refugees need to be evacuated? "))

num_trips = math.ceil(num_refugees / capacity)

# Display number of trips needed
print(f"\n{num_trips} trips are needed to evacuate all the refugees.")

total_evacuated = 0
for trip in range(1, num_trips+1):
    if trip < num_trips:
        num_to_evacuate = capacity
    else:
        num_to_evacuate = num_refugees - total_evacuated
    # Update total number of refugees evacuated so far
    total_evacuated += num_to_evacuate
    
    print(f"\nRefugee Report for Trip #{trip}")
    print(f"{num_to_evacuate} refugees were evacuated on this trip.")
    print(f"{total_evacuated} refugees have been evacuated so far.")
