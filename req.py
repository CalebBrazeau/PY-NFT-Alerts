import Get_Info as info
import Get_Con as conn
import Send_Alert as alert
import creds

# Initialize array to store retreived information
arr = []
# Name of the collection to retreive information from
collection_name = "mintin"
# Maximum price of NFT to add to array
maxSOL = 2

def main():
    # Get listing information from API for collection
    listingInfo = info.getListingInfo(collection_name)
    # Get listed count from returned data
    listedCount = listingInfo["listedCount"]

    # Initialize offset variable used in connection request
    offset = 0

    while offset < listedCount:
        # Get collection using collection name and offset to eventually retreive all listed NFT's
        returnData = conn.getConnection("/v2/collections/" + collection_name + "/listings?offset=" + str(offset) + "&limit=20")
        # Loop through returned request data
        for x in returnData:
            # If the price of the current element is less than the maximum set
            if(x["price"] <= maxSOL):
                # Add it to the array.
                arr.append(
                    {
                        'price': x["price"],
                        'link': 'https://magiceden.io/item-details/' + x["tokenMint"]
                    }
                )
        # Increase offset to eventually end loop
        offset += 20
    # Sort array using price as a key
    arr.sort(key=arrSortKey)
    
    # Subject for alert
    subject = "Alert for %s Collection!" % (collection_name)
    # Body for alert containing the array of retreived NFT's
    alert_content = """\n
    The following prices were alerted for %s: %s
    """ % (collection_name, formatArr(arr))
    # Send the alert
    alert.sendAlert(subject, alert_content, creds.email)


def formatArr(arr):
    """Takes in an array and formats the objects to a more user friendly string"""
    # Initialize string
    formatedArr = ""
    # Loop through each element of the array
    for x in arr:
        # Append a seperator to formatedArr for easier readability
        formatedArr += "\n------------------------------------------------------------------------------------"
        # Loop through each element's keys
        for y in x.keys():
            # Add each key with a prepended new line and keyname to formatedArr
            formatedArr += "\n%s: %s" % (y,x[y])
    print(formatedArr) # TEMP
    # Return the formated array
    return formatedArr


def arrSortKey(e):
    """Sort array of retreived NFT's from lowest to highest price"""
    return e["price"]


main()