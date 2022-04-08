import Get_Info as info
import Send_Alert as alert
import creds

collection_name = "mintin" # Collection you want alerts for
minFP = 1.5 # Minimum Floor Price to be alerted on

def main():
    # Get Listing info for specified collection
    listingInfo = info.getListingInfo(collection_name)
    # If the collections floor price is greater than specified minimum
    if(listingInfo["floorPrice"] / 1000000000 >= minFP):
        # Send Floor Price alert
        alert.sendAlert("Floor Price Alert!", """
        \nFloor price for %s, was detected above %s SOL.\nFloor Price: %s SOL """ % (collection_name, minFP, listingInfo["floorPrice"] / 1000000000), creds.email)
main()