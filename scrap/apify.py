from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("<YOUR_API_TOKEN>")

# Prepare the Actor input
run_input = {
    "search": "New York",
    "startUrls": None,
    "maxItems": 10,
    "propertyType": "none",
    "sortBy": "distance_from_search",
    "minScore": None,
    "starsCountFilter": "any",
    "currency": "USD",
    "language": "en-gb",
    "checkIn": None,
    "checkOut": None,
    "flexWindow": None,
    "rooms": 1,
    "adults": 2,
    "children": 0,
    "minMaxPrice": "0-999999",
}

# Run the Actor and wait for it to finish
run = client.actor("QGcJvQyG9NqMKTYPH").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
