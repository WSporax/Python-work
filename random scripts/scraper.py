# from bs4 import BeautifulSoup
# import requests

# userdata = {"Username": "hussam67", "password": "Rasp55rips"}
# resp = requests.get('https://vle.aston.ac.uk/ultra/course', data = userdata)
import sys, requests

def check_link(my_url):
    try:
        requests.get(my_url#, verify=False
        )
        print("Valid URL")
    except IOError:
        print("Invalid URL")
        sys.exit()
html = requests.get(user_url)