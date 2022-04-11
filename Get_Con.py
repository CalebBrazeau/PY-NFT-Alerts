import http.client
import json

def getConnection(link):
    """
    Takes in last part of magic eden api and returns API response data

    link = /v2/launchpad/collections?offset=0&limit=200

    Returns json object containing API response
    """
    # Open intial connection to magiceden API
    conn = http.client.HTTPSConnection("api-mainnet.magiceden.dev")
    # Send request for specified link
    conn.request("GET", link, "", {})
    # Get request response
    res = conn.getresponse()
    # Read response
    data = res.read()
    # Convert read response data to json object and return
    return json.loads(data.decode("utf-8"))