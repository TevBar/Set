# Our airline's flight destinations
our_routes = {"LAX", "JFK", "CDG", "DXB"}

# Competitor airline's flight destinations
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations both airlines fly to
shared_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", shared_destinations)

# 2. Destinations unique to our airline
unique_our_routes = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_our_routes)

# 3. Are there destinations that neither airline shares?
exclusive_destinations = our_routes.isdisjoint(competitor_routes)
if exclusive_destinations:
    print("There are destinations that neither airline shares.")
else:
    print("Both airlines share some destinations.")
