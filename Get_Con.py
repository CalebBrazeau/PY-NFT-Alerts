import http.client
import json

def getConnection(link):
    conn = http.client.HTTPSConnection("api-mainnet.magiceden.dev")
    conn.request("GET", link, "", {})
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))