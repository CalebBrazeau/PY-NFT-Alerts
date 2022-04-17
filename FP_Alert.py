import Get_Info as info
import Send_Alert as alert
import creds

collection_name = "mintin" # Collection you want alerts for
min_FP = 2 # Minimum Floor Price to be alerted on

def main():
    # Get Listing info for specified collection
    listing_info = info.getListingInfo(collection_name)
    # If the collections floor price is greater than specified minimum
    if(listing_info["floorPrice"] / 1000000000 >= min_FP):
        # Send Floor Price alert
        alert.sendAlert("Floor Price Alert!", """
        \nFloor price for %s, was detected above %s SOL.\nFloor Price: %s SOL """ % (collection_name, min_FP, listing_info["floorPrice"] / 1000000000), creds.email)
main()