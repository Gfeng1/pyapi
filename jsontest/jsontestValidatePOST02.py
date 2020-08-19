#!/usr/bin/python3

import requests

# define the URL we want to use
TIMEURL = "http://date.jsontest.com/"
IPURL = "http://ip.jsontest.com/"
VALIDURL = "http://validate.jsontest.com/"

def main():
    # use requests library to send an HTTP GET
    resp = requests.get(TIMEURL)
    resp2 = requests.get(IPURL)
    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()
    respjson2 = resp2.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)
    print(respjson2)

    # JUST display the value of "ip"
    print(f"The current Time is --> {respjson['time']}")
    print(f"The current WAN IP is --> {respjson2['ip']}")
    
    with open("myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    jsonToTest = {}
    jsonToTest["time"] = respjson
    jsonToTest["ip"] = respjson2
    jsonToTest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsonToTest)

    resp3 = requests.post(VALIDURL, data=mydata)
    respjson3 = resp3.json() 
    
    print(respjson3)

    print(f"Is your JSON valid? {respjson3['validate']}")

if __name__ == "__main__":
    main()
