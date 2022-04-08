import Get_Info as info
import Get_Con as conn
import Send_Alert as alert
import creds

arr = []
collection_name = "mintin"
maxSOL = 2

def main():
    listingInfo = info.getListingInfo(collection_name)
    listedCount = listingInfo["listedCount"]

    offset = 0
    while offset < listedCount:
        returnData = conn.getConnection("/v2/collections/" + collection_name + "/listings?offset=" + str(offset) + "&limit=20")
        for x in returnData:
            if(x["price"] <= maxSOL):
                arr.append(
                    {
                        'price': x["price"],
                        'link': 'https://magiceden.io/item-details/' + x["tokenMint"]
                    }
                )
        offset += 20
    
    arr.sort(key=arrSortKey)
    
    subject = "Alert for %s Collection!" % (collection_name)
    alert_content = """\n
    The following prices were alerted for %s: %s
    """ % (collection_name, formatArr(arr))
    
    alert.sendAlert(subject, alert_content, creds.email)


def formatArr(arr):
    formatedArr = ""
    for x in arr:
        formatedArr += "\n------------------------------------------------------------------------------------"
        for y in x.keys():
            formatedArr += "\n%s: %s" % (y,x[y])
    print(formatedArr)
    return formatedArr


def arrSortKey(e):
    return e["price"]


main()