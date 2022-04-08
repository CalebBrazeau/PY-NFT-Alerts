import http.client
import json

def getConnection(link):
    """Return request data from magiceden API for specified link"""
    # Open intial connection to magiceden API
    conn = http.client.HTTPSConnection("api-mainnet.magiceden.dev")
    # Send request for specified link (/v2/tokens/{token})
    conn.request("GET", link, "", {})
    # Get request response
    res = conn.getresponse()
    # Read response
    data = res.read()
    # Convert read response data to json object and return
    return json.loads(data.decode("utf-8"))