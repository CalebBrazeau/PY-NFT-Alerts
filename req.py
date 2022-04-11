import Get_Info as info
import Send_Alert as alert
import creds

# Name of the collection to retreive information from
collection_name = "mintin".replace(" ", "_")
# Maximum price of NFT to add to array
maxSOL = 2


def main():
    # Array containing specified collection return data
    arr = info.getCollectionListed(collection_name, maxSOL)

    # Check if return is empty before sending alert
    if(len(arr) > 0):
        # Sort array using price as a key
        arr.sort(key=arrSortKey)

        # Subject for alert
        subject = "%s listing alerted for %s Collection!" % (len(arr), collection_name)
        # Body for alert containing the array of retreived NFT's
        alert_content = """\n
        The following prices were alerted for %s: %s
        """ % (collection_name, formatArr(arr))
        # Send the alert
        alert.sendAlert(subject, alert_content, creds.email)


def formatArr(arr):
    """
    Takes in an array and formats the objects to a more user friendly string
    Input: [{'price': 2, 'link': 'www.example.com'}, {'price': 2, 'link': 'www.example.com'}]
    Return: -------------------------------------------------------------
            price: 2
            link: www.example.com
            -------------------------------------------------------------
            price: 2
            link: www.example.com
    """
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