import Get_Con as conn
import datetime


def getListingInfo(collection_name):
    """Takes in a collection name and returns listing stats for specified collection"""
    # Get and return API response for collection stats
    return conn.getConnection("/v2/collections/" + collection_name.lower() + "/stats")


def getTokenInformation(token):
    """Takes in a token address and returns information about specified token"""
    # Get and return API response for token information
    return conn.getConnection("/v2/tokens/" + token)


def getLaunchpadInfo():
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
        except: # Throws if there is no launch date
            print("No time :/")
    return arr


def getCollectionListed(name, max):
    """Takes in name and max number of SOL and returns array containing all listings under or equal to maximum amount of SOL"""
    # Initialize empty array
    arr = []
    # Get listing information from API for collection
    listingInfo = getListingInfo(name.lower())
    # Get listed count from returned data
    listedCount = listingInfo["listedCount"]

    # Initialize offset variable used in connection request
    offset = 0

    while offset < listedCount:
        # Get collection using collection name and offset to eventually retreive all listed NFT's
        data = conn.getConnection("/v2/collections/" + name.lower() + "/listings?offset=" + str(offset) + "&limit=20")
        # Loop through returned request data
        for x in data:
            # If the price of the current element is less than the maximum set
            if(x["price"] <= max):
                # Add it to the array.
                arr.append(
                    {
                        'name': getTokenInformation(x['tokenMint'])['name'],
                        'price': str(x["price"]) + " SOL",
                        'link': 'https://magiceden.io/item-details/' + x["tokenMint"]
                    }
                )
        # Increase offset to eventually end loop
        offset += 20
    return arr