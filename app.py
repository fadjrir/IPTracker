#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib3
import json
import sys
import time
import os

__banner__ = """
  ___ ___ _____            _           
 |_ _| _ \_   _| _ __ _ __| |_____ _ _ 
  | ||  _/ | || '_/ _` / _| / / -_) '_|
 |___|_|   |_||_| \__,_\__|_\_\___|_|  
  IPTracker Tool's by Fadjri_
"""

def main():
    os.system("clear")
    print(__banner__)
    BASE_PATH_URL = "https://api.indoxploit.or.id/ip/"
    r = requests.Session()
    urllib3.disable_warnings()
    try:
        ip = str(input("[?] IP Tracking: "))
        if (ip == ""):
            print("Oops! Invalid input, please try again.")
            sys.exit(1)
            pass
        else:
            print("\n> Process: Tracking IP Address at '" + ip + "' ....")
            time.sleep(1)
            pass
        try:
            regx = r.get(BASE_PATH_URL + ip, timeout=30, verify=False)
            data = json.loads(regx.text)
            if (data["error"] == True):
                print("Oops! IP Address at '" + ip + "' not found, please try again!")
                sys.exit(1)
                pass
            else:
                print("> Process: Successfully! Tracking IP Address at '" + ip + "' ....")
                time.sleep(1)
                pass
            print("\n -------------- TRACKING RESULT --------------")
            print(" > IP Address: " + str(data["data"]["geolocation"][0]["query"]))
            print(" > Hostnames: " +
                str(data["data"]["geolocation"][0]["reverse"]))
            print(" > ASN: " + str(data["data"]["geolocation"][0]["as"]))
            print(" > ISP: " + str(data["data"]["geolocation"][0]["isp"]))
            print(" > Organization: " + str(data["data"]["geolocation"][0]["org"]))
            print(" > Continent: " +
                str(data["data"]["geolocation"][0]["timezone"]))
            print(" > Country: " +
                str(data["data"]["geolocation"][0]["country"]) + "/" +
                str(data["data"]["geolocation"][0]["countryCode"]))
            print(" > State/Region: " +
                str(data["data"]["geolocation"][0]["regionName"]) + "/" +
                str(data["data"]["geolocation"][0]["region"]))
            print(" > City: " + str(data["data"]["geolocation"][0]["city"]))
            print(" > Latitude: " + str(data["data"]["geolocation"][0]["lat"]))
            print(" > Longitude: " + str(data["data"]["geolocation"][0]["lon"]))
            print(" ----------------------------------------------\n")
            pass
        except requests.exceptions.ConnectTimeout:
            pass
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.ReadTimeout:
            pass
    except KeyboardInterrupt:
        sys.exit(1)
        pass
    pass

if __name__ == "__main__":
    main()
    pass
