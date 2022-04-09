import Get_Con as conn
import datetime


def getLaunchpad():
    """Retrieves and returns all upcoming collections on the launchpad"""
    # Initialize array to store retreived collections
    arr = []
    # Get and return API request for launchpad items
    data = conn.getConnection("/v2/launchpad/collections?offset=0&limit=200")

    # Loop through all items in the API response
    for x in data:
        try:
            # Extract year, month, and day information from each element
            y,m,d = x["launchDatetime"].split("-")
            # Create datetime variable using extracted year, month, and day
            launch_time = datetime.datetime(int(y),int(m),int(d.split("T")[0]))
            # Get current time for comparison
            now = datetime.datetime.now()

            # If the launch time of the collection is greater than the current time
            if(launch_time > now):
                # Append the collection to the array
                arr.append({
                    'name': x['name'],
                    'price': x['price'],
                    'size': x['size'],
                    'launchTime': launch_time
                })
        except:
            print("No time :/")
    return arr