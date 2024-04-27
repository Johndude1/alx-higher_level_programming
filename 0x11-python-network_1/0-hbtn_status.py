#!/usr/bin/python3
import urllib.request

def fetch_status():
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
    print("- Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
if __name__ == "__main__":
    fetch_status()
