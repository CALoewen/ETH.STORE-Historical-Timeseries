import requests
import time

base_url = "https://beaconcha.in/api/v1/ethstore/"

start_day = 0  # Replace with your desired start day
end_day = 1  # Replace with your desired end day
rate_limit = 10  # Requests per minute

# Calculate the time to wait between requests based on the rate limit
time_to_wait = 60 / rate_limit

for beaconchain_day in range(start_day, end_day + 1):
    url = f"{base_url}{beaconchain_day}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  
        print(f"Data for Beaconchain Day {beaconchain_day}:")
        print(data)
    else:
        print(f"Failed to retrieve data for Beaconchain Day {beaconchain_day}")

    time.sleep(time_to_wait)