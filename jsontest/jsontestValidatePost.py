#!/usr/bin/env python3
import requests

# define the URL we want to use
TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"
VALIDURL = "http://validate.jsontest.com/"


def getTimeJSON():
    try:
       time_response = requests.get(TIMEURL)
       if time_response.status_code != 200:
           raise Exception
       return time_response.json().get("time")
    except Exception as time_api_error:
        print("Fail to connect TIME API")
        print(time_api_error)


def getIPAddressJSON():
    try:
        ip_address_response = requests.get(IPURL)
        if ip_address_response.status_code != 200:
            raise Exception
        return ip_address_response.json().get("ip")
    except Exception as ip_address_api_error:
        print("Fail to connect IP API")
        print(ip_address_api_error)


def readTextFile(filename):
    try:
        with open(filename) as myserver:
            myserver_text = myserver.readlines()
        return myserver_text
    except FileNotFoundError:
        print("Fail to open the file")


def formatIntoJSON(time, ip, server_text):
    json_data = {
        "time": time,
        "ip": ip,
        "server": server_text
    }
    return json_data


def main():
    # Part A
    current_time = getTimeJSON()
    # Part B
    current_ip = getIPAddressJSON()
    # Part C
    read_text = readTextFile("./myservers.txt")
    # Part D
    formattedJsonData = formatIntoJSON(current_time, current_ip, read_text)
    # Part E
    # Post to validate the data
    # need a key
    formatDataToPost = {
        "json": str(formattedJsonData)
    }
    post_call_back = requests.post(VALIDURL, data=formatDataToPost)
    print(post_call_back)
    if (post_call_back.status_code != 200):
        print("Fail to post")
    else:
        post_call_back_json = post_call_back.json()
        print(f"IS valid JSON? {post_call_back_json.get('validate')}")


if __name__ == "__main__":
    main()
