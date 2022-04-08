import Get_Con as conn

def getListingInfo(collection_name):
    data = conn.getConnection("/v2/collections/" + collection_name + "/stats")
    return data


def getTokenImage(token):
    data = conn.getConnection("/v2/tokens/" + token)
    return data