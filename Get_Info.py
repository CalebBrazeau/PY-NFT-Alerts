import Get_Con as conn

def getListingInfo(collection_name):
    """Takes in a collection name and returns listing stats for specified collection"""
    # Get and return API response for collection stats
    return conn.getConnection("/v2/collections/" + collection_name + "/stats")


def getTokenInformation(token):
    """Takes in a token address and returns information about specified token"""
    # Get and return API response for token information
    return conn.getConnection("/v2/tokens/" + token)